from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List
import json
import os
import uvicorn
import requests
import urllib.parse
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Marker(BaseModel):
    id: str
    x: float
    y: float
    type: str
    name: str
    image: Optional[str] = None
    source: Optional[str] = "local" # We still call it local to re-use frontend styles

DATA_FILE = "shared_pins.json"

class SharedData(BaseModel):
    markers: List[dict]
    deleted_ids: List[str]

DATA_FILE = "shared_pins.json"
GLOBAL_FILE = "dataset.json"

def load_shared_data() -> SharedData:
    if not os.path.exists(DATA_FILE):
        return SharedData(markers=[], deleted_ids=[])
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Support old format
            if isinstance(data, list):
                return SharedData(markers=data, deleted_ids=[])
            return SharedData(**data)
    except Exception as e:
        print(f"Error loading {DATA_FILE}: {e}")
        return SharedData(markers=[], deleted_ids=[])

def save_shared_data(data: SharedData):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            # Use model_dump_json for v2, fallback to json for v1
            if hasattr(data, "model_dump_json"):
                f.write(data.model_dump_json(indent=2))
            else:
                f.write(data.json(indent=2))
    except Exception as e:
        print(f"Error saving {DATA_FILE}: {e}")

def load_global_markers() -> List[dict]:
    if not os.path.exists(GLOBAL_FILE):
        return []
    try:
        with open(GLOBAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {GLOBAL_FILE}: {e}")
        return []

@app.get("/api/pins")
def get_pins():
    global_markers = load_global_markers()
    shared = load_shared_data()
    
    # 1. Filter out deleted global markers
    merged = [m for m in global_markers if m["id"] not in shared.deleted_ids]
    
    # 2. Map shared markers by ID for quick lookup
    shared_lookup = {m["id"]: m for m in shared.markers}
    
    # 3. Apply updates to global markers and add new ones
    final_list = []
    
    # For global markers, if there's an update in shared, use it
    for gm in merged:
        if gm["id"] in shared_lookup:
            final_list.append(shared_lookup[gm["id"]])
            del shared_lookup[gm["id"]]
        else:
            final_list.append({**gm, "source": "global"})
            
    # Add remaining shared markers (new ones)
    for sm in shared_lookup.values():
        final_list.append({**sm, "source": "local"})
        
    return final_list

@app.post("/api/pins")
def add_pin(pin: Marker):
    print(f"UDATING PIN: {pin.id} ({pin.name})") # DEBUG
    shared = load_shared_data()
    # Remove if exists in shared
    shared.markers = [m for m in shared.markers if m["id"] != pin.id]
    
    # Use model_dump for v2, fallback to dict for v1
    if hasattr(pin, "model_dump"):
        pin_dict = pin.model_dump()
    else:
        pin_dict = pin.dict()

    # Ensure it's not in deleted_ids if it's being updated/re-added
    if pin.id in shared.deleted_ids:
        shared.deleted_ids.remove(pin.id)
        
    shared.markers.append(pin_dict)
    save_shared_data(shared)
    return {"status": "success", "pin": pin_dict}

@app.delete("/api/pins/{pin_id}")
def delete_pin(pin_id: str):
    shared = load_shared_data()
    
    # Check if it was in shared markers
    originally_in_shared = any(m["id"] == pin_id for m in shared.markers)
    shared.markers = [m for m in shared.markers if m["id"] != pin_id]
    
    # Check if it was a global marker
    global_markers = load_global_markers()
    is_global = any(m["id"] == pin_id for m in global_markers)
    
    if is_global and pin_id not in shared.deleted_ids:
        shared.deleted_ids.append(pin_id)
        
    save_shared_data(shared)
    return {"status": "success"}

@app.post("/api/pins/purge")
def purge_pins():
    save_shared_data(SharedData(markers=[], deleted_ids=[]))
    return {"status": "purged"}

WIKI_CACHE = {}

@app.get("/api/wiki/{location}")
def get_wiki_info(location: str):
    if location in WIKI_CACHE:
        return WIKI_CACHE[location]

    try:
        url = f"https://miscreated.fandom.com/api.php?action=parse&page={urllib.parse.quote(location)}&prop=text&format=json"
        res = requests.get(url, timeout=5)
        data = res.json()
        if 'parse' not in data: 
            return {"error": "No wiki page found for this location."}
        
        html = data['parse']['text']['*']
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove infoboxes and navboxes
        for unwanted in soup.find_all(['aside', 'table']):
            unwanted.decompose()
            
        summary = ""
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if text:
                summary += text + "\n\n"
            if len(summary) > 150:
                break
        summary = summary.strip()
                
        # Try to find an image
        image = None
        img_tag = soup.find('img', class_='pi-image-thumbnail') or soup.find('img', class_='thumbimage') or soup.find('img')
        if img_tag and (img_tag.has_attr('src') or img_tag.has_attr('data-src')):
            raw_src = img_tag.get('data-src') or img_tag.get('src')
            if raw_src and raw_src.startswith('http'):
                image = raw_src.split('/revision/latest')[0]
                
        result = {"summary": summary, "image": image}
        WIKI_CACHE[location] = result
        return result
    except Exception as e:
        return {"error": str(e)}

# Serve the static files (index.html, map.jpg, dataset.json) from the current directory
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True, log_level="info")

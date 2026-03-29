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
import re

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
    source: Optional[str] = "local"
    found: Optional[bool] = False

class Diplomacy(BaseModel):
    id: str
    name: str
    status: str # ally, enemy, neutral, nap
    notes: Optional[str] = ""
    last_updated: Optional[str] = None

DATA_FILE = "shared_pins.json"
GLOBAL_FILE = "dataset.json"

class SharedData(BaseModel):
    markers: List[dict] = []
    deleted_ids: List[str] = []
    diplomacy: List[dict] = []
    deleted_diplomacy_ids: List[str] = []


    def __init__(self, **data):
        super().__init__(**data)

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
    handled_ids = set()
    
    # 3. Apply updates to global markers and add new ones
    final_list = []
    
    # For global markers, if there's an update in shared, use it
    for gm in merged:
        if gm["id"] in shared_lookup:
            final_list.append(shared_lookup[gm["id"]])
            handled_ids.add(gm["id"])
        else:
            final_list.append({**gm, "source": "global"})
            
    # Add remaining shared markers (new ones)
    for sm in shared.markers:
        if sm["id"] not in handled_ids:
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
    save_shared_data(SharedData(markers=[], deleted_ids=[], diplomacy=[], deleted_diplomacy_ids=[]))
    return {"status": "purged"}

@app.get("/api/diplomacy")
def get_diplomacy():
    shared = load_shared_data()
    return [r for r in shared.diplomacy if r["id"] not in shared.deleted_diplomacy_ids]

@app.post("/api/diplomacy")
def add_diplomacy(relation: Diplomacy):
    shared = load_shared_data()
    # Update or Add
    shared.diplomacy = [r for r in shared.diplomacy if r["id"] != relation.id]
    
    if hasattr(relation, "model_dump"):
        rel_dict = relation.model_dump()
    else:
        rel_dict = relation.dict()
        
    # Ensure it's not in deleted_diplomacy_ids if re-added
    if relation.id in shared.deleted_diplomacy_ids:
        shared.deleted_diplomacy_ids.remove(relation.id)
        
    shared.diplomacy.append(rel_dict)
    save_shared_data(shared)
    return {"status": "success", "relation": rel_dict}

@app.delete("/api/diplomacy/{rel_id}")
def delete_diplomacy(rel_id: str):
    shared = load_shared_data()
    shared.diplomacy = [r for r in shared.diplomacy if r["id"] != rel_id]
    
    # Track as deleted to ensure consistency with static mode exports
    if rel_id not in shared.deleted_diplomacy_ids:
        shared.deleted_diplomacy_ids.append(rel_id)
        
    save_shared_data(shared)
    return {"status": "success"}

WIKI_CACHE = {}

@app.get("/api/wiki/{location}")
def get_wiki_info(location: str):
    if location in WIKI_CACHE:
        return WIKI_CACHE[location]

    # Skip generic names that won't have unique wiki pages
    blocked_names = [
        "car", "vehicle spawn", "tent", "tents", "cave", "stash", "hidden stash",
        "my base", "base", "wreck", "gas station", "tower", "tunnel", 
        "point of interest", "boat spawn", "weapon cache", "military outpost", "bunker",
        "unknown", "new marker", "house", "crate", "loot"
    ]
    if location.lower() in blocked_names:
        return {"error": "Generic name skipped"}

    def scrap_page(query: str):
        try:
            url = f"https://miscreated.fandom.com/api.php?action=parse&page={urllib.parse.quote(query)}&prop=text&format=json"
            res = requests.get(url, timeout=5)
            data = res.json()
            if 'parse' not in data: 
                return None
            
            html = data['parse']['text']['*']
            soup = BeautifulSoup(html, 'html.parser')
            
            # Remove infoboxes, navboxes, and galleries
            for unwanted in soup.find_all(['aside', 'table', 'div', 'script']):
                if 'gallery' in unwanted.get('class', []) or 'navbox' in unwanted.get('class', []) or 'portable-infobox' in unwanted.get('class', []):
                    unwanted.decompose()
                elif unwanted.name == 'aside' or unwanted.name == 'table':
                    unwanted.decompose()
                    
            summary_parts = []
            for p in soup.find_all('p'):
                text = p.get_text().strip()
                # Remove reference brackets like [1], [12], etc.
                text = re.sub(r'\[[0-9]+\]', '', text)
                if text and len(text) > 20: # Skip short fragments
                    summary_parts.append(text)
                if len("\n\n".join(summary_parts)) > 250:
                    break
            summary = "\n\n".join(summary_parts).strip()
                    
            # Try to find a good image (thumbnail / infobox)
            image = None
            # Prioritize standard wiki image selectors
            img_tag = soup.find('img', class_='pi-image-thumbnail') or soup.find('img', class_='thumbimage') or soup.find('img')
            if img_tag and (img_tag.has_attr('src') or img_tag.has_attr('data-src')):
                raw_src = img_tag.get('data-src') or img_tag.get('src')
                if raw_src and raw_src.startswith('http'):
                    # Clean up the URL to get the original/latest version
                    image = raw_src.split('/revision/latest')[0]
                    
            if not summary: return None
            return {"summary": summary, "image": image}
        except:
            return None

    # Try direct name
    result = scrap_page(location)
    
    # Try fallback: split the name and try the first word/prefix (e.g. "Woodhaven Bunker" -> "Woodhaven")
    if not result:
        # Check if the name contains common sub-location words
        keywords = ["Bunker", "Tents", "Camp", "Base", "Military", "Checkpoint", "Station", "Radio"]
        match = re.match(r"^(.+?)\s+(?:" + "|".join(keywords) + ")", location, re.IGNORECASE)
        if match:
            fallback_query = match.group(1).strip()
            result = scrap_page(fallback_query)

    if not result:
        return {"error": f"No wiki page found for '{location}'."}
        
    WIKI_CACHE[location] = result
    return result

# Serve the static files (index.html, map.jpg, dataset.json) from the current directory
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True, log_level="info")

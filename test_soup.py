import requests
from bs4 import BeautifulSoup
import json

def get_wiki_info(title):
    try:
        url = f"https://miscreated.fandom.com/api.php?action=parse&page={title}&prop=text&format=json"
        res = requests.get(url, timeout=5)
        data = res.json()
        if 'parse' not in data: return {"error": "No parse in response"}
        
        html = data['parse']['text']['*']
        soup = BeautifulSoup(html, 'html.parser')
        
        summary = None
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if text and len(text) > 20:
                summary = text
                break
                
        image = None
        img_tag = soup.find('img', class_='pi-image-thumbnail') or soup.find('img', class_='thumbimage') or soup.find('img')
        if img_tag and (img_tag.has_attr('src') or img_tag.has_attr('data-src')):
            raw_src = img_tag.get('data-src') or img_tag.get('src')
            if raw_src and raw_src.startswith('http'):
                image = raw_src.split('/revision/latest')[0] + '/revision/latest'
                
        return {"summary": summary, "image": image}
    except Exception as e:
        return {"error": str(e)}

print("Brightmoor:", json.dumps(get_wiki_info("Brightmoor"), indent=2))
print("Hayward Valley:", json.dumps(get_wiki_info("Hayward Valley"), indent=2))

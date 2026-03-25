import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

new_css = """  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Inter:wght@400;500;600&display=swap');

  :root {
    --bg-dark: #0f172a;
    --panel-bg: rgba(15, 20, 30, 0.65);
    --panel-border: rgba(255, 255, 255, 0.08);
    --text-main: #f8fafc;
    --text-muted: #cbd5e1;
    --accent: #d4af37;
    --accent-hover: #f1c40f;
    --danger: #ef4444;
  }

  body { 
    margin: 0; 
    font-family: 'Inter', system-ui, sans-serif; 
    background: #020617; 
    color: var(--text-main); 
    display: block; 
    height: 100vh; 
    overflow: hidden; 
    font-size: 14px;
  }

  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.15); border-radius: 4px; }
  ::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.3); }

  /* Map and Layout */
  #mapWrap { 
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    overflow: hidden; 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    background: #000; 
    cursor: crosshair; 
    z-index: 1;
  }
  #mapWrap:active { cursor: crosshair; }
  
  #mapContainer { 
    position: relative; 
    width: 100%; 
    max-width: none; 
    transform-origin: 50% 50%;
  }
  
  img#mapImage { 
    width: 100%; 
    height: auto; 
    display: block; 
    pointer-events: none; 
  }
  
  #overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; }
  
  /* Sidebar */
  #sidebar { 
    position: absolute;
    left: 24px;
    top: 80px;
    bottom: 24px;
    width: 320px; 
    background: var(--panel-bg); 
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--panel-border); 
    border-radius: 16px;
    padding: 24px; 
    overflow-y: auto; 
    z-index: 10; 
    display: flex;
    flex-direction: column;
    gap: 24px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.4s ease;
  }

  #sidebar.collapsed {
    transform: translateX(-120%);
    opacity: 0;
    pointer-events: none;
  }

  /* Main Toggle Button */
  #sidebarToggle {
    position: absolute;
    left: 24px;
    top: 24px;
    z-index: 20;
    width: 44px;
    height: 44px;
    background: var(--panel-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--panel-border);
    border-radius: 12px;
    color: var(--accent);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 16px rgba(0,0,0,0.3);
    transition: all 0.2s ease;
  }
  #sidebarToggle:hover {
    background: rgba(255,255,255,0.1);
    transform: scale(1.05);
    color: var(--accent-hover);
  }

  .sidebar-section {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  
  /* Typography */
  h1, h2, h3, h4 { 
    margin: 0;
    color: var(--accent);
    font-family: 'Cinzel', serif;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
  }

  /* Form Elements */
  button, select, input[type="text"], input[type="file"] { 
    width: 100%;
    margin: 0; 
    padding: 10px 12px; 
    border: 1px solid rgba(255,255,255,0.15); 
    border-radius: 8px; 
    background: rgba(0, 0, 0, 0.3); 
    color: var(--text-main); 
    font-family: inherit; 
    font-size: 14px; 
    outline: none; 
    box-sizing: border-box;
    transition: all 0.2s ease;
  }
  
  input::placeholder { color: rgba(255,255,255,0.4); }
  
  select:focus, input[type="text"]:focus {
    border-color: var(--accent);
    background: rgba(0,0,0,0.5);
    box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.2);
  }

  button { 
    cursor: pointer; 
    background: var(--accent); 
    color: #000;
    border: none;
    font-weight: 600;
    font-family: 'Cinzel', serif;
    letter-spacing: 0.05em;
  }
  button:hover { background: var(--accent-hover); box-shadow: 0 0 12px rgba(212, 175, 55, 0.4); transform: translateY(-1px); }
  button:active { transform: translateY(0); }
  
  button.danger { background: rgba(239, 68, 68, 0.1); border: 1px solid var(--danger); color: var(--danger); box-shadow: none; font-family: 'Inter', sans-serif;}
  button.danger:hover { background: var(--danger); color: #fff; box-shadow: 0 0 12px rgba(239, 68, 68, 0.4); }

  button.outline { background: transparent; border: 1px solid rgba(255,255,255,0.2); color: var(--text-main); font-family: 'Inter', sans-serif; }
  button.outline:hover { background: rgba(255,255,255,0.1); color: #fff; }

  /* Filters & Lists */
  .filter { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; cursor: pointer; font-size: 14px; user-select: none; transition: color 0.2s; }
  .filter:hover { color: #fff; }
  .filter input { width: auto; margin: 0; cursor: pointer; accent-color: var(--accent); }
  
  ul { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; }
  li { 
    padding: 10px 14px; 
    background: rgba(0, 0, 0, 0.2); 
    border: 1px solid rgba(255,255,255,0.05); 
    border-radius: 8px;
    display: flex; 
    justify-content: space-between; 
    align-items: center; 
    cursor: pointer; 
    transition: all 0.2s; 
  }
  li:hover { border-color: var(--accent); background: rgba(0, 0, 0, 0.4); box-shadow: 0 4px 12px rgba(0,0,0,0.2); transform: translateX(4px); }
  
  .delete-btn { width: auto; padding: 4px 8px; border-radius: 6px; margin-left: 8px; font-family: 'Inter', sans-serif; }
  .pin-name { flex: 1; pointer-events: none; font-weight: 500; font-family: 'Inter', sans-serif; }
  
  /* Map Markers and Labels */
  .marker { 
    position: absolute; 
    transform: translate(-50%, -50%); 
    font-size: 24px; 
    cursor: pointer; 
    z-index: 2; 
    pointer-events: auto;
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); 
    filter: drop-shadow(0 4px 6px rgba(0,0,0,0.6)); 
  }
  .marker:hover { transform: translate(-50%, -50%) scale(1.4); z-index: 3; }
  
  .label { 
    position: absolute; 
    font-family: 'Cinzel', serif;
    font-size: 13px; 
    font-weight: 700;
    letter-spacing: 0.05em;
    background: rgba(10, 15, 20, 0.8); 
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    color: var(--accent); 
    padding: 6px 10px; 
    border-radius: 8px; 
    border: 1px solid rgba(212, 175, 55, 0.3); 
    transform: translate(-50%, -200%); 
    white-space: nowrap; 
    pointer-events: none; 
    z-index: 2; 
    box-shadow: 0 4px 16px rgba(0,0,0,0.4); 
    text-transform: uppercase;
  }
  
  /* Modals and Info Cards */
  .modal-bg { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.8); z-index: 100; align-items: center; justify-content: center; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }
  .modal { background: var(--panel-bg); padding: 32px; border: 1px solid var(--panel-border); border-radius: 20px; width: 340px; box-shadow: 0 24px 48px rgba(0,0,0,0.6); display: flex; flex-direction: column; gap: 16px; position: relative; }
  
  #infoCard { display: none; position: absolute; right: 24px; top: 24px; background: var(--panel-bg); padding: 32px; border: 1px solid var(--panel-border); border-radius: 20px; width: 300px; box-shadow: 0 24px 48px rgba(0,0,0,0.6); z-index: 90; backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); }
  
  .card-close { position: absolute; right: 20px; top: 20px; width: auto; background: transparent !important; color: rgba(255,255,255,0.5); padding: 4px; border: none !important; margin: 0; box-shadow: none !important; }
  .card-close:hover { color: #fff; transform: scale(1.1); background: transparent !important; }
  
  #infoName { font-family: 'Cinzel', serif; font-size: 22px; color: var(--accent); margin-bottom: 6px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
  #infoType { color: rgba(255,255,255,0.7); font-size: 13px; font-weight: 500; text-transform: uppercase; margin-bottom: 20px; letter-spacing: 0.1em; font-family: 'Inter', sans-serif;}
  
  #infoWikiText {
    font-size: 14px;
    color: var(--text-muted);
    line-height: 1.6;
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid rgba(255,255,255,0.1);
    display: none;
    font-family: 'Inter', sans-serif;
  }
  
  .panel-box { display: flex; flex-direction: column; gap: 12px; }"""

# Replace entire style block
content = re.sub(r"<style>.*?</style>", f"<style>\n{new_css}\n</style>", content, flags=re.DOTALL)

# Insert toggle button right before <div id="sidebar">
toggle_html = '''<button id="sidebarToggle" onclick="document.getElementById('sidebar').classList.toggle('collapsed')">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
</button>

<div id="sidebar">'''
content = content.replace('<div id="sidebar">', toggle_html)

# Update font inline styles
content = content.replace('style="color: #fff; font-size: 16px;"', 'style="color: var(--accent); font-size: 18px;"')
content = content.replace('style="color: #fff; font-size: 14px;"', 'style="color: var(--accent); font-size: 16px;"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")

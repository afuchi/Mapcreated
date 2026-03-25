import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update JS data types
text = text.replace(
    "let filters = { car: true, military: true, bunker: true, tent: true, cave: true, stash: true, home: true };",
    "let filters = { car: true, military: true, bunker: true, tent: true, cave: true, stash: true, home: true, wreck: true, gas: true, tower: true, tunnel: true };"
)
text = text.replace(
    "const icons = { car: '🚗', military: '🔫', bunker: '🧱', tent: '⛺', cave: '🕳️', stash: '📦', home: '🏠' };",
    "const icons = { car: '🚗', military: '🔫', bunker: '🧱', tent: '⛺', cave: '🕳️', stash: '📦', home: '🏠', wreck: '🛩️', gas: '⛽', tower: '🗼', tunnel: '🚇' };"
)
text = text.replace(
    "const defaultNames = { car: 'Car Spawn', military: 'Military Camp', bunker: 'Bunker', tent: 'Tents', cave: 'Cave', stash: 'Hidden Stash', home: 'My Base' };",
    "const defaultNames = { car: 'Car Spawn', military: 'Military Camp', bunker: 'Bunker', tent: 'Tents', cave: 'Cave', stash: 'Hidden Stash', home: 'My Base', wreck: 'Wreck', gas: 'Gas Station', tower: 'Tower', tunnel: 'Tunnel' };"
)

# 2. Update `<select id="typeSelect">`
select_html = """        <option value="cave">🕳️ Cave</option>
        <option value="stash">📦 Stash</option>
        <option value="wreck">🛩️ Wreck</option>
        <option value="gas">⛽ Gas Station</option>
        <option value="tower">🗼 Tower</option>
        <option value="tunnel">🚇 Tunnel</option>
        <option value="home">🏠 Base</option>"""
text = re.sub(r'<option value="cave">.*?</option>\s*<option value="stash">.*?</option>\s*<option value="home">.*?</option>', select_html, text, flags=re.DOTALL)

# 3. Update filters panel
filters_html = """      <label class="filter"><input type="checkbox" checked onchange="toggleFilter('cave')"> 🕳️ Caves</label>
      <label class="filter"><input type="checkbox" checked onchange="toggleFilter('stash')"> 📦 Stashes</label>
      <label class="filter"><input type="checkbox" checked onchange="toggleFilter('wreck')"> 🛩️ Wrecks</label>
      <label class="filter"><input type="checkbox" checked onchange="toggleFilter('gas')"> ⛽ Gas Stations</label>
      <label class="filter"><input type="checkbox" checked onchange="toggleFilter('tower')"> 🗼 Towers</label>
      <label class="filter"><input type="checkbox" checked onchange="toggleFilter('tunnel')"> 🚇 Tunnels</label>
      <label class="filter"><input type="checkbox" checked onchange="toggleFilter('home')"> 🏠 Bases</label>"""
text = re.sub(r'<label class="filter"><input type="checkbox" checked onchange="toggleFilter\(\'cave\'\)".*?</label>\s*<label class="filter"><input type="checkbox" checked onchange="toggleFilter\(\'stash\'\)".*?</label>\s*<label class="filter"><input type="checkbox" checked onchange="toggleFilter\(\'home\'\)".*?</label>', filters_html, text, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated index.html categories.")

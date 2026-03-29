# 🗺️ Miscreated Intel Map — v4.4.4 "Ultimate Edition"

An advanced, high-performance intelligence mapping suite for **Miscreated**, built for tactical coordination and long-term world persistence.

---

## ✨ Features

### 📍 Tactical Marker System
- **14+ Marker Types**: Track 🚗 Vehicles, 🏰 Military bases, 🧱 Bunkers, 📦 Stashes, ⛵ Boats, and more.
- **Dynamic Context**: Automated **Wiki Integration** fetches live summaries and images from the official Miscreated Fandom Wiki for any location (including user-created ones!).
- **Interactivity**: Fluid drag-and-drop repositioning for all custom markers.
- **Progression**: Mark pins as "Found" or "Tracked" to visually dim them and keep your map clean.

### 👥 Diplomacy & Relations
- **Faction Tracking**: Dedicated tab for managing player and clan relations.
- **Status Tags**: Categorize contacts as 🟢 Ally, 🔴 Hostile, or ⚪ Neutral with Nap (Non-Aggression Pact) support.
- **Encounter Notes**: Store detailed intel on player encounters, gear, and known locations.

### 🔍 Search & Filtering
- **Global Search**: Instantly find markers or player relations by name, type, or notes.
- **Smart Filtering**: Multi-column filter grid with "Hide Found" toggle to focus only on what remains to be discovered.
- **Collapsible Groups**: Markers are organized into clean, categorized groups with live count badges.

### ⚡ Performance & UX
- **Glassmorphic UI**: Premium dark mode design with cinematic typography (`Cinzel`) and smooth transitions.
- **Smart Scaling**: Map markers automatically scale inversely to zoom levels, ensuring they never block your view.
- **Clamped Navigation**: Precise pan/zoom (via `Panzoom`) with boundary enforcement.

---

## 🚀 Getting Started

The Intel Map can be run as a **Collaborative Server** (Synced) or a **Static Portfolio** (GitHub Pages).

### 🖥️ Running as a Collaborative Server (Recommended)
This mode allows multiple users to view and edit the same map state in real-time.

**Requirements**: Python 3.9+

1. **Initialize Environment**:
   ```powershell
   ./setup_env.ps1
   ```
2. **Launch Server**:
   ```powershell
   python server.py
   ```
3. **Access**: Navigate to `http://localhost:8000` in your browser.

### 🌐 Static Hosting (GitHub Pages)
The map is fully compatible with static hosting. Changes are persisted to the browser's `localStorage` and can be exported as a JSON file.

- **Import/Export**: Use the **Settings ⚙️** tab to export your `shared_pins.json` for manual backup or repository syncing.
- **Fallback**: If the API is unavailable, the map seamlessly transitions to local storage mode.

---

## 🛠️ Technology Stack
- **Frontend**: Vanilla JavaScript (ES6+), HTML5, CSS3 (Custom Glassmorphism)
- **Engine**: [Panzoom.js](https://github.com/timmywil/panzoom) for high-performance map interaction.
- **Backend**: FastAPI (Python) for real-time synchronization.
- **Data**: JSON-based persistence (`shared_pins.json` & `dataset.json`).
- **Scraper**: BeautifulSoup4 for on-the-fly Wiki intel.

---

## 📂 Project Structure
- `index.html`: The core application and UI logic (2000+ lines of optimized code).
- `server.py`: FastAPI backend handling Wiki scraping and JSON persistence.
- `shared_pins.json`: The live database of player-created markers and diplomacy.
- `dataset.json`: Static database of hardcoded world locations.
- `map.jpg`: High-resolution Orca Island / Miscreated world map.

---

> [!TIP]
> **Pro-Tip**: When creating a pin for a town like "Woodhaven", naming it exactly after the location will automatically trigger the Wiki Context scraper, providing you with lore and reference images instantly.

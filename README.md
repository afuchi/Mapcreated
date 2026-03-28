# Miscreated Intel Map — v3.3

An interactive, browser-based intelligence map for the survival game **Miscreated**.

---

## Features

### 🗺️ Interactive Map
- Smooth pan and zoom with mouse wheel
- Map is clamped to boundaries — can't pan off the edge
- Clicking the map focuses on the selected location with a smooth animated zoom

### 📍 Marker System
- Place custom markers anywhere on the map via the **v3.3** panel
- Choose from 14 marker types: 🚗 Car, 🏰 Military, 🧱 Bunker, ⛺ Tent, 🕳️ Cave, 📦 Stash, 🛩️ Wreck, ⛽ Gas, 🗼 Tower, 🚇 Tunnel, 📍 Location, 🏠 Base, ⛵ Boat, 🔫 Weapon
- Custom marker name and optional image attachment
- Drag and drop any marker to reposition it on the map

### 📋 Sidebar — Collapsible Groups
- All pins are organized into **collapsible type groups** (e.g. Bunkers, Boats, Gas Stations)
- Each group shows a live **count badge**
- Click a group header to expand or collapse it
- Delete individual custom (Shared Live) markers directly from the list

### 🔍 Filters
- Toggle individual pin types on/off with checkboxes in a **2-column grid**
- **Show All** — checks all filters at once
- **Clear Filters** — unchecks all filters at once

### 📐 Smart Pin Scaling
- Pins automatically scale down as you zoom in, so they never obscure the map beneath them

### 🌐 Wiki Integration
- Clicking a 📍 Location pin fetches a live summary and image from the [Miscreated Wiki](https://miscreated.fandom.com) and displays it in an info card

### 🔄 Shared Live Data (requires Python server)
- Markers placed are synced to a local backend (`shared_pins.json`) in real time
- Polling every 3 seconds keeps all connected users in sync
- **Purge Shared Data** button wipes all custom markers for everyone

---

## Running Locally

Requires **Python 3.8+**.

1. Run the setup script to install dependencies:
   ```powershell
   ./setup_env.ps1
   ```

2. Start the server:
   ```powershell
   ./venv/Scripts/python server.py
   ```

3. Open your browser and go to `http://localhost:8000`

---

## Static Hosting (GitHub Pages)

The map works without a Python backend on static hosts like **GitHub Pages**.

- On GitHub Pages, only `shared_pins.json` is loaded — this is the single source of truth for all pins displayed
- To update pins on GitHub Pages, run the server locally, position your pins, then push `shared_pins.json` to GitHub

> **Note:** Live sharing and drag-save features require the Python server to be running.

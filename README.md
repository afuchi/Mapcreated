# Miscreated Intel Map

A fully interactive, dynamic web map for the game **Miscreated**. 

## Features
- **Extensive Marker Dataset**: Includes dynamic mapping for Cars, Military outposts, Bunkers, Tents, Caves, Stashes, Bases, Wrecks, Gas Stations, Radio Towers, Tunnels, and more!
- **Interactive Drag & Drop**: Easily place and move custom markers on the map visually, automatically locking the map pan while you configure spots.
- **Shared Live Data**: Any custom pins placed on the map are synced with a local backend database for connected users, grouped into the "Global Data" sidebar list. You can visually arrange them, delete them, or purge them!
- **Lore Integration**: Locked location markers (📍) automatically fetch layout pictures and lore summaries directly from the official Miscreated Wiki when clicked on!
- **Dynamic View Optimization**: Deep-zoom marker scaling automatically shrinks pin icons when you zoom in so you never lose sight of your surroundings underneath huge markers. 
- **Filtering System**: Toggle individual asset categories independently from the sidebar to easily find exactly what you're looking for.

## Local Setup
You will need exactly two things to run this map backend locally:
1. Windows Powershell
2. Python 3.8+

Run the included `setup_env.ps1` script to install the FastAPI dependencies within a protected virtual environment:
```powershell
./setup_env.ps1
```

## Running the Server
The simplest way to start the local map server is by executing `server.py` using your new virtual environment:
```powershell
./venv/Scripts/python server.py
```
The application will start an HTTP Python FastAPI server on your machine.
Simply open your web browser and navigate to `http://localhost:8000/` to test out the Map!

## Static Hosting (GitHub Pages)
Because the map is designed to fall back to natively reading from `dataset.json` when the Python API isn't around, this map can flawlessly host itself entirely free inside static delivery services like **GitHub Pages** without any backend server required! 

*(Note that the "Shared Live" updating and marker drag/drop saving features require the active Python API to be running)*.

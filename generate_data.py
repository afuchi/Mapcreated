import json

data = []
ctx = {"idx": 1}

def add_point(x, y, type_, name):
    data.append({"id": str(ctx["idx"]), "x": x, "y": y, "type": type_, "name": name})
    ctx["idx"] += 1

# Bunkers
bunkers = [
    (8, 55, "Turtle Bay Bunker"),
    (16, 58, "Woodhaven Bunker 1"),
    (18, 60, "Woodhaven Bunker 2"),
    (12, 73, "Horseshoe Beach Bunker"),
    (18, 85, "South West Bunker"),
    (25, 71, "Sultan Bunker 1"),
    (27, 76, "Sultan Bunker 2"),
    (30, 84, "South Sultan Bunker"),
    (45, 76, "Pinecrest Bunker"),
    (47, 82, "South Pinecrest Bunker"),
    (62, 73, "Brightmoor Bunker 1"),
    (65, 71, "Brightmoor Bunker 2"),
    (74, 89, "Lumber Yard Bunker"),
    (86, 39, "Cape Bay Bunker 1"),
    (89, 44, "Cape Bay Bunker 2"),
    (87, 38, "Cape Bay Bunker 3"),
    (70, 40, "Orca Dam Bunker"),
    (57, 42, "Clyde Hill Bunker"),
    (43, 22, "Hayward Valley Bunker 1"),
    (44, 24, "Hayward Valley Bunker 2"),
    (47, 24, "Hayward Valley Bunker 3"),
    (43, 28, "Hayward Valley Bunker 4"),
    (45, 27, "Hayward Valley Bunker 5"),
    (48, 26, "Hayward Valley Bunker 6"),
    (42, 32, "Hayward Valley Bunker 7"),
    (45, 33, "Hayward Valley Bunker 8"),
    (52, 54, "Center Map Bunker"),
    (40, 52, "West Center Bunker"),
    (31, 28, "West Hayward Bunker"),
    (25, 31, "North West River Bunker")
]
for x, y, name in bunkers: add_point(x, y, "bunker", name)

# Tents
tents = [
    (15, 48, "North Woodhaven Tents"),
    (18, 54, "Woodhaven Tents 1"),
    (20, 58, "Woodhaven Tents 2"),
    (15, 60, "South Woodhaven Tents"),
    (23, 82, "Airfield Tents"),
    (8, 71, "Horseshoe Beach Tents"),
    (28, 75, "Sultan Tents 1"),
    (31, 82, "South Sultan Tents"),
    (45, 85, "Pinecrest Tents"),
    (50, 89, "South Pinecrest Tents"),
    (55, 70, "West Brightmoor Tents"),
    (60, 74, "Brightmoor Tents"),
    (40, 14, "North Hayward Tents"),
    (34, 16, "Far North Tents"),
    (45, 20, "Hayward Valley Tents 1"),
    (42, 35, "Hayward Valley Tents 2"),
    (44, 40, "South Hayward Tents"),
    (40, 48, "NW Center Tents"),
    (47, 49, "North Center Tents"),
    (42, 52, "West Center Tents"),
    (45, 58, "South Center Tents"),
    (50, 53, "East Center Tents"),
    (55, 58, "Far East Center Tents"),
    (68, 30, "North Orca Dam Tents"),
    (70, 40, "Orca Dam Tents"),
    (68, 48, "South Orca Dam Tents"),
    (30, 42, "West River Tents"),
    (35, 52, "Cave Park Tents"),
    (21, 68, "River Fork Tents")
]
for x, y, name in tents: add_point(x, y, "tent", name)

# Vehicles (Combined and specific names)
vehicles = [
    (45, 22, "Hayward Valley Car"),
    (46, 25, "Hayward Valley Bus"),
    (44, 28, "Hayward Valley Sedan"),
    (38, 25, "West Hayward Car"),
    (62, 75, "Brightmoor Sedan"),
    (65, 72, "Brightmoor Shore Car"),
    (88, 40, "Cape Bay Sedan"),
    (43, 80, "Pinecrest Car"),
    (25, 78, "Sultan Pick-Up"),
    (18, 62, "Woodhaven Sedan"),
    (35, 12, "North Hayward Truck"),
    (40, 44, "Cedar Park Bus"),
    (42, 48, "Cedar Park Car"),
    (48, 43, "Cedar Park Pick-Up"),
    (31, 56, "West Center Car"),
    (17, 84, "Airfield Cargo Truck"),
    (22, 85, "Airfield Bus"),
    (20, 86, "Airfield ATV"),
    (18, 82, "Airfield Pick-Up"),
    (34, 84, "Pinecrest West Car"),
    (45, 82, "Pinecrest East Car"),
    (49, 86, "South Pinecrest Car"),
    (67, 82, "Brightmoor East Car"),
    (55, 68, "Lumber Yard Truck"),
    (55, 58, "Center Route Car"),
    (78, 28, "NE Coast Car"),
    (15, 88, "Sultan Outskirts Car"),
    (62, 28, "North Orca Dam Car"),
    (60, 45, "Clyde Hill Outskirts Car"),
    (45, 26, "Hayward Valley Police Car"),
    (44, 24, "Hayward Valley Taxi"),
    (28, 73, "Sultan Tractor"),
    (26, 70, "Sultan Baggage Cart"),
    (14, 56, "Woodhaven Buggy"),
    (16, 54, "Woodhaven Sedan")
]
for x, y, name in vehicles: add_point(x, y, "car", name)

# Boats (NEW)
boats = [
    (12, 56, "Turtle Bay Boat"),
    (18, 65, "Woodhaven Coast Boat"),
    (26, 35, "West River Boat"),
    (28, 75, "Sultan Dock Boat"),
    (32, 65, "Center River Boat"),
    (42, 52, "Lake Boat 1"),
    (45, 50, "Lake Boat 2"),
    (66, 72, "Brightmoor Shore Boat"),
    (78, 55, "East Coast Boat 1"),
    (82, 45, "East Coast Boat 2"),
    (38, 2, "North Shore Boat"),
    (92, 48, "Cape Bay Shore Boat"),
    (8, 52, "Turtle Bay North Boat"),
    (20, 92, "Airfield Coast Boat")
]
for x, y, name in boats: add_point(x, y, "boat", name)

# Weapons/Military (NEW Differentiation)
military_outposts = [
    (20, 84, "Amalgamated Airfield Command"),
    (30, 60, "Radio Tower Military"),
    (65, 30, "North East Military Array"),
    (75, 88, "South East Military Checkpoint"),
    (35, 32, "West Center Military"),
    (12, 50, "Far West Military Base"),
    (11, 53, "Turtle Bay Base"),
    (58, 20, "NE Military Array"),
    (45, 10, "Far North Military"),
    (54, 87, "Far South Military"),
    (18, 12, "Orca Hospital Military Guard"),
    (86, 38, "Cape Bay Checkpoint"),
    (48, 88, "Pinecrest Perimeter"),
    (28, 42, "Hayward Distributors Command")
]
for x, y, name in military_outposts: add_point(x, y, "military", name)

weapons = [
    (46, 23, "Hayward Valley Weapon Cache"),
    (15, 58, "Woodhaven Weapon Cache"),
    (28, 72, "Sultan Weapon Cache"),
    (64, 75, "Brightmoor Weapon Cache"),
    (22, 14, "Hospital Weapon Cache"),
    (42, 46, "Cedar Park Weapon Cache"),
    (72, 42, "Orca Dam Weapon Cache"),
    (38, 56, "Center Cave Weapon Cache"),
    (88, 38, "Cape Bay Weapon Cache"),
    (52, 50, "Crest Derby Weapon Cache"),
    (75, 85, "Lumber Yard Weapon Cache"),
    (14, 22, "North Watch Weapon Cache")
]
for x, y, name in weapons: add_point(x, y, "weapon", name)

# Caves
caves = [
    (28, 68, "West River Cave"),
    (29, 30, "West Hayward Cave"),
    (45, 22, "North Hayward Cave"),
    (67, 82, "Brightmoor Cave"),
    (35, 56, "Center Cave"),
    (42, 92, "South Coast Cave"),
    (7, 50, "Turtle Bay Coastal Cave"),
    (60, 25, "East Ridge Cave"),
    (55, 80, "Southeast Deep Cave")
]
for x, y, name in caves: add_point(x, y, "cave", name)

# Wrecks
wrecks = [
    (36, 58, "Center Plane Wreck"),
    (54, 22, "North Clyde Plane Wreck"),
    (82, 30, "Brightmoor Plane Wreck"),
    (21, 43, "West Coast Shipwreck"),
    (19, 74, "Sultan Coast Shipwreck"),
    (44, 94, "South Coast Shipwreck"),
    (58, 8, "Far North Shipwreck"),
    (84, 20, "NE Coast Shipwreck"),
    (28, 98, "SW Coastal Plane Wreck"),
    (74, 52, "Lake Plane Wreck")
]
for x, y, name in wrecks: add_point(x, y, "wreck", name)

# Gas Stations
gas_stations = [
    (16, 18, "Far NW Gas Station"),
    (35, 45, "Cedar Park Gas Station"),
    (26, 75, "Haven Gas Station"),
    (46, 52, "Center Map Gas Station"),
    (15, 88, "Sultan Gas Station"),
    (78, 28, "NE Coast Gas Station"),
    (64, 72, "Brightmoor Gas"),
    (45, 24, "Hayward Valley Main Gas"),
    (22, 56, "Woodhaven Outlet Gas")
]
for x, y, name in gas_stations: add_point(x, y, "gas", name)

# Towers
towers = [
    (36, 35, "Hayward Water Tower"),
    (48, 32, "North Center Water Tower"),
    (21, 75, "Sultan Water Tower"),
    (64, 78, "Brightmoor Water Tower"),
    (64, 66, "North Brightmoor Water Tower"),
    (58, 28, "North Orca Radio Tower"),
    (28, 64, "Center Radio Tower"),
    (17, 21, "NW Radio Tower"),
    (85, 45, "Cape Bay Radio Tower"),
    (8, 52, "Turtle Bay Radio Tower"),
    (18, 53, "Woodhaven Comm Tower"),
    (21, 13, "Orca Hospital Antenna"),
    (18, 88, "Airfield Tower"),
    (40, 45, "Cedar Park Radio Relay"),
    (45, 82, "Pinecrest Signal Tower")
]
for x, y, name in towers: add_point(x, y, "tower", name)

# Tunnels
tunnels = [
    (21, 32, "West Hayward Tunnel"),
    (22, 80, "Sultan Road Tunnel"),
    (32, 14, "North Hayward Tunnel"),
    (55, 30, "East Mountain Tunnel"),
    (40, 72, "South Pass Tunnel")
]
for x, y, name in tunnels: add_point(x, y, "tunnel", name)

# Locations
locations = [
    (46, 22, "Hayward Valley"),
    (14, 58, "Woodhaven"),
    (41, 84, "Pinecrest"),
    (88, 40, "Cape Bay"),
    (64, 74, "Brightmoor"),
    (28, 71, "Sultan"),
    (12, 53, "Turtle Bay"),
    (10, 72, "Horseshoe Beach"),
    (43, 45, "Cedar Park"),
    (58, 42, "Clyde Hill"),
    (20, 84, "Amalgamated Airfield"),
    (75, 88, "Lumber Yard"),
    (70, 42, "Orca Dam"),
    (18, 12, "Orca Hospital"),
    (27, 30, "West Hayward Trailer Park"),
    (30, 45, "River Trailer Park"),
    (58, 70, "Brightmoor Trailer Park"),
    (66, 70, "Brightmoor Shore"),
    (50, 88, "Forest Valley Road"),
    (18, 22, "NW River Cabins"),
    (35, 12, "North Watch"),
    (28, 40, "Hayward Distributors")
]
for x, y, name in locations: add_point(x, y, "location", name)

with open('dataset.json', 'w') as f:
    json.dump(data, f, indent=2)
print(f"Saved dataset.json with {len(data)} locations.")

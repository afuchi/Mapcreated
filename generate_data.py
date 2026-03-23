import json

data = []
idx = 1

def add_point(x, y, type_, name):
    global idx
    data.append({"id": str(idx), "x": x, "y": y, "type": type_, "name": name})
    idx += 1

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

for x, y, name in bunkers:
    add_point(x, y, "bunker", name)

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

for x, y, name in tents:
    add_point(x, y, "tent", name)

# A few Cars from the master map
cars = [
    (45, 22, "Hayward Valley Cars"),
    (46, 25, "Hayward Valley Cars 2"),
    (44, 28, "Hayward Valley Cars 3"),
    (38, 25, "West Hayward Cars"),
    (62, 75, "Brightmoor Cars"),
    (65, 72, "Brightmoor Shore Cars"),
    (88, 40, "Cape Bay Cars"),
    (43, 80, "Pinecrest Cars"),
    (25, 78, "Sultan Cars"),
    (18, 62, "Woodhaven Cars")
]
for x, y, name in cars:
    add_point(x, y, "car", name)

# A few military spots
military = [
    (20, 90, "Amalgamated Airfield"),
    (30, 60, "Radio Tower Military"),
    (65, 30, "North East Military Array"),
    (75, 88, "South East Military Checkpoint"),
    (35, 32, "West Center Military"),
    (12, 50, "Far West Military Base")
]
for x, y, name in military:
    add_point(x, y, "military", name)

with open('dataset.json', 'w') as f:
    json.dump(data, f, indent=2)
print("Saved dataset.json")

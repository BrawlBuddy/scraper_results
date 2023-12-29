import json
import os

all_results = list()
map_mode = set()

# importing the results
for file in os.scandir():
    if file.name.split(".")[-1] == "json":
        with open(file.name, "r") as f:
            result = json.load(f)
            all_results.extend(result)

for battle in all_results:
    map_mode.add((battle['battle_map'],battle['battle_mode']))

with open("final_results/maps_modes.json","w") as f:
    json.dump(list(map_mode),f)
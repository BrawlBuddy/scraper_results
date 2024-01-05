import os 
import json

complete_results = []

for file in os.scandir():
    if file.name.split('.')[1] == "json":
        with open(file, "r") as f:
            complete_results.extend(json.load(f))


with open("scrapper_out.json", "w") as f:
    json.dump(complete_results, f)

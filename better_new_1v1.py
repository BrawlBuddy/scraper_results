import os
import json
from itertools import product

result_jsons = ['AD.json', 'AF.json', 'AL.json', 'AS.json', 'DZ.json']

all_merged_results = list()
timestamps = dict()
win_rates = dict()

for file_name in result_jsons:
    with open(file_name, "r") as f:
        temp_result = json.load(f)
        all_merged_results.extend(temp_result)

for entry in all_merged_results:
    
    combinations = list(product(entry["team_A"], entry["team_B"]))

    for brawler_pair in combinations:
        pair = list(brawler_pair)
        pair.sort()
        pair_record = timestamps.get('_'.join(pair))
        if pair_record == None:
            pair_record = {
                "wins": set(),
                "games": set()
            }
        pair_record["games"].add(entry["battle_time"])
        if entry["team_A_wins"] ^ (pair[0] in entry["team_B"]):
            pair_record["wins"].add(entry["battle_time"])
        
        timestamps['_'.join(pair)] = pair_record
    

for brawler in list(timestamps.keys()):
    win_rates[brawler] = len(timestamps[brawler]['wins'])/len(timestamps[brawler]['games'])

with open("1v1.json", "w") as f:
    json.dump(win_rates, f)

    


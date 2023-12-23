import json
import os


all_results = list()
converted_results = dict()



# importing the results
for file in os.scandir():
    if file.name.split(".")[-1] == "json":
        with open(file.name, "r") as f:
            result = json.load(f)
            all_results.extend(result)



'''
Cases:
    Team A wins - not inverted -> player1 wins
    Team A wins - inverted -> player1 doesn't win
    Team A loses - not inverted -> player1 doesn't win
    Team A loses - inverted -> player1 wins
'''


# finding all possiblities
for battle in all_results:
    for team_A_brawler in battle['team_A']:
        for team_B_brawler in battle['team_B']:
            flipped = False
            team_combo = [team_A_brawler,team_B_brawler]
            original = '-'.join(team_combo)
            team_combo.sort()
            key = '_'.join(team_combo)
            if key != original:
                flipped = True
            player_1_wins = battle['team_A_wins']^flipped #XOR
            existing_record_brawlers = converted_results.get(key)
            if existing_record_brawlers == None:
                converted_results[key] = dict()
                existing_record_brawlers = {
                    battle["battle_mode"]: {
                        "player1_wins":set(),
                        "player2_wins":set()
                    }
                }
            existing_record_mode = existing_record_brawlers.get(battle["battle_mode"])
            if existing_record_mode == None:
                existing_record_mode = {
                    "player1_wins":set(),
                    "player2_wins":set()
                }
            if player_1_wins:
                existing_record_mode["player1_wins"].add(battle["battle_time"])
            else:
                existing_record_mode["player2_wins"].add(battle["battle_time"])
            converted_results[key][battle["battle_mode"]] = existing_record_mode

serializable_result = dict()

for brawler_pair in converted_results.keys():
    serializable_result[brawler_pair] = dict()
    for mode in converted_results[brawler_pair].keys():
        serializable_result[brawler_pair][mode] = {
            "player1_wins": list(converted_results[brawler_pair][mode]['player1_wins']),
            "player2_wins": list(converted_results[brawler_pair][mode]['player2_wins'])
        }
    

with open("first_draft.json", "w") as f_out:
    json.dump(serializable_result, f_out)

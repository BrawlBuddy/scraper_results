import json

with open("scrapper_out.json", "r") as f:
    all_battles = json.load(f)

output_result = dict()
interm_result = dict() 
max_rate = 0
for battle in all_battles:
    game_map = battle["battle_map"]
    team_A = battle["team_A"]
    team_B = battle["team_B"]
    team_A_wins = battle["team_A_wins"]
    battle_time = battle["battle_time"]
    if interm_result.get(game_map) == None:
        interm_result[game_map] = dict()
    for brawler_A in team_A:
        current_result = interm_result[game_map].get(brawler_A)
        if current_result == None:
            current_result = {
            "wins": set(),
            "games": set()
            }
        if team_A_wins:
            current_result['wins'].add(battle_time)
        current_result['games'].add(battle_time)
        interm_result[game_map][brawler_A] = current_result
    
    for brawler_B in team_B:
        current_result = interm_result[game_map].get(brawler_B)
        if current_result == None:
            current_result = {
            "wins": set(),
            "games": set()
            }
        if team_A_wins:
            current_result['wins'].add(battle_time)
        current_result['games'].add(battle_time)
        interm_result[game_map][brawler_B] = current_result



for game_map in interm_result.keys():
    output_result[game_map] = dict()
    for brawler in interm_result[game_map].keys():
        val = interm_result[game_map][brawler]
        win_rate = len(val['wins'])/len(val['games'])
        output_result[game_map][brawler] = win_rate

with open("map.json", "w") as f:
    json.dump(output_result,f)



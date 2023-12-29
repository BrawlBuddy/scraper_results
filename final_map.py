import json

with open("calculated_tables/1v1map.json", "r") as f:
    loaded_result = json.load(f)

output_result = dict()
interm_result = dict() 
max_rate = 0
for game_map in loaded_result.keys():
    interm_result[game_map] = dict()
    wins = 0
    games = 0
    for brawler in loaded_result[game_map].keys():
        brawlers = brawler.split('_')
        # brawler 1
        current_result = interm_result[game_map].get(brawlers[0])
        if current_result == None:
            wins = 0
            games = 0
        else:
            wins = current_result[0]
            games = current_result[1]
        wins += len(loaded_result[game_map][brawler]['player1_wins'])
        games += len(loaded_result[game_map][brawler]['player1_wins'])+len(loaded_result[game_map][brawler]['player2_wins'])
        interm_result[game_map][brawlers[0]] = (wins,games)
         # brawler 2
        current_result = interm_result[game_map].get(brawlers[1])
        if current_result == None:
            wins = 0
            games = 0
        else:
            wins = current_result[0]
            games = current_result[1]
        wins += len(loaded_result[game_map][brawler]['player2_wins'])
        games += len(loaded_result[game_map][brawler]['player1_wins'])+len(loaded_result[game_map][brawler]['player2_wins'])
        interm_result[game_map][brawlers[1]] = (wins,games)

print(interm_result)
    
max_win_rate = 0

for game_map in interm_result.keys():
    output_result[game_map] = dict()
    for brawler in interm_result[game_map].keys():
        val = interm_result[game_map][brawler]
        win_rate = val[0]/val[1]
        if max_win_rate < win_rate:
            max_win_rate = win_rate
        output_result[game_map][brawler] = win_rate

print(max_win_rate)

with open("final_results/map.json", "w") as f:
    json.dump(output_result,f)

'''
    win_rate = wins/games
    output_result[game_map] = win_rate
    # debugging, really weird that the all of the win rates are so low, however some of the winrates are >50 which makes me think its right??? idk need to review
    if win_rate > max_rate:
        max_rate = win_rate
    #print((len(loaded_result[key1]['player1_wins']),len(loaded_result[key1]['player2_wins']),win_rate))

print(max_rate)

with open("final_results/map.json", "w") as f:
    json.dump(output_result,f)
'''

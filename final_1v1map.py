import json

with open("calculated_tables/1v1map.json", "r") as f:
    loaded_result = json.load(f)

output_result = dict()

max_rate = 0
for game_map in loaded_result.keys():
    for brawler in loaded_result[game_map].keys():
        win_rate = len(loaded_result[game_map][brawler]['player1_wins'])/(len(loaded_result[game_map][brawler]['player1_wins'])+len(loaded_result[game_map][brawler]['player2_wins']))
        if output_result.get(game_map) == None:
            output_result[game_map] = dict()
        output_result[game_map][brawler] = win_rate

        # debugging, really weird that the all of the win rates are so low, however some of the winrates are >50 which makes me think its right??? idk need to review
        if win_rate > max_rate:
            max_rate = win_rate
        #print((len(loaded_result[key1]['player1_wins']),len(loaded_result[key1]['player2_wins']),win_rate))

print(max_rate)

with open("final_results/1v1map.json", "w") as f:
    json.dump(output_result,f)

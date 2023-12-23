import json

def find_all_winrates(brawler_name, dataset):
    brawler_results = dict()
    for key in dataset.keys():
        split_names = key.split('_')
        if brawler_name in split_names:
            player_1_wins = len(dataset[key]['player1_wins'])
            player_2_wins = len(dataset[key]['player2_wins'])
            if brawler_name == split_names[0]:
                brawler_results[split_names[1]] = ((player_1_wins,player_1_wins+player_2_wins))
            else:
                brawler_results[split_names[0]] = ((player_2_wins,player_1_wins+player_2_wins))

    return brawler_results

def best_for_three(brawler_array, dataset):
    # I want to implement some way of accounting for the number of results scored, to promote more clearly confimred results, not sure how to do this
    #alpha = 0.1 
    scored_brawlers = dict()
    for brawler in brawler_array:
        current_brawler_result = find_all_winrates(brawler,dataset)
        for key in current_brawler_result.keys():
            current_score = scored_brawlers.get(key)
            if current_score == None:
                current_score = (1-current_brawler_result[key][0]/current_brawler_result[key][1])
            else:
                current_score += (1-current_brawler_result[key][0]/current_brawler_result[key][1])
            scored_brawlers[key] = current_score
    return sorted(scored_brawlers.items(), key=lambda x: x[1],  reverse=True)
    
    # I don't think i need the line below
    #scores_for_all = set(all_brawler_results[0].keys()).union(set(all_brawler_results[1].keys())).union(set(all_brawler_results[2].keys())) 
    




with open("calculated_tables/1v1.json", "r") as f:
    loaded_result = json.load(f)
    

print(find_all_winrates("RUFFS",loaded_result))
#print(best_for_three(["RUFFS", "BO", "OTIS"], loaded_result))
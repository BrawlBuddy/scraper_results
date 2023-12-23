import json

def find_all_winrates(brawler_name, game_mode, dataset):
    brawler_results = dict()
    for key in dataset.keys():
        split_names = key.split('_')
        if brawler_name in split_names:
            mode_result = dataset[key][game_mode]
            if mode_result == None:
                continue

            player_1_wins = len(dataset[key][game_mode]['player1_wins'])
            player_2_wins = len(dataset[key][game_mode]['player2_wins'])
            if brawler_name == split_names[0]:
                brawler_results[split_names[1]] = ((player_1_wins,player_1_wins+player_2_wins))
            else:
                brawler_results[split_names[0]] = ((player_2_wins,player_1_wins+player_2_wins))

    return brawler_results




with open("calculated_tables/1v1mode.json", "r") as f:
    loaded_result = json.load(f)


print(find_all_winrates("HANK", "brawlBall", loaded_result))
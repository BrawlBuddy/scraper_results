import json

result_jsons = ['AD.json', 'AF.json', 'AL.json', 'AS.json', 'DZ.json']

all_merged_results = list()


for file_name in result_jsons:
    with open(file_name, "r") as f:
        temp_result = json.load(f)
        all_merged_results.extend(temp_result)


def find_1v1_win_rate(brawler1, brawler2):
    brawler1_wins = 0
    battles = 0

    
    for battle in all_merged_results:
        #brawler1 on team_A case
        if brawler1 in battle["team_A"]:
            if brawler2 in battle["team_B"]:
                battles += 1
                if battle["team_A_wins"]:
                    brawler1_wins += 1
        
        #brawler1 on team_B case
        if brawler1 in battle["team_B"]:
            if brawler2 in battle["team_A"]:
                battles += 1
                if not battle["team_A_wins"]:
                    brawler1_wins += 1

    win_rate = brawler1_wins/battles
    return win_rate



with open("final_results/1v1.json", "r") as f:
    old_result = json.load(f)

brawler_matchups = old_result.keys()

max_win_rate = 0
min_win_rate = 1

new_1v1 = dict()
for matchup in list(brawler_matchups):
    split_matchup = matchup.split('_')
    current_wr = find_1v1_win_rate(split_matchup[0], split_matchup[1])

    new_1v1[matchup] = current_wr

with open("final_results/new_1v1.json","w") as f:
    json.dump(new_1v1, f)
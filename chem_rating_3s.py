import json

all_merged_results = list()



with open("scrapper_out.json", "r") as f:
    all_merged_results = json.load(f)

threesome_chem = dict()

for battle in all_merged_results:
    #team_A
    battle["team_A"].sort()
    teamA = '_'.join(battle["team_A"])
    current_count = threesome_chem.get(teamA)
    if current_count == None:
        wins = 0
        games = 0
    games += 1
    if battle['team_A_wins']:
        wins += 1
    threesome_chem[teamA] = (wins,games)
    
    #team_B
    battle["team_B"].sort()
    teamB = '_'.join(battle["team_B"])
    current_count = threesome_chem.get(teamB)
    if current_count == None:
        wins = 0
        games = 0
    games += 1
    if not battle['team_A_wins']:
        wins += 1
    threesome_chem[teamB] = (wins,games)

with open("3scores.json", "w") as f:
    json.dump(threesome_chem, f)
        

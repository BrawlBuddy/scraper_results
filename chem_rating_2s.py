import json

all_merged_results = list()

with open("scrapper_out.json", "r") as f:
    all_merged_results = json.load(f)

duo_chem = dict()

for battle in all_merged_results:
    if len(battle["team_A"]) != 3 or len(battle["team_B"]) != 3:
        continue
    #team_A
    teamA_all = battle["team_A"]

    teamA_all.sort()
    teamA_combos = [f"{teamA_all[0]}_{teamA_all[1]}",f"{teamA_all[1]}_{teamA_all[2]}",f"{teamA_all[0]}_{teamA_all[2]}"]

    for duoA in teamA_combos:
        current_count = duo_chem.get(duoA)
        if current_count == None:
            wins = 0
            games = 0
        games += 1
        if battle['team_A_wins']:
            wins += 1
        duo_chem[duoA] = (wins,games)
    
    #team_B
    teamB_all = battle["team_B"]
    teamB_all.sort()
    teamB_combos = [f"{teamB_all[0]}_{teamB_all[1]}",f"{teamB_all[1]}_{teamB_all[2]}",f"{teamB_all[0]}_{teamB_all[2]}"]
    for duoB in teamB_combos:
        current_count = duo_chem.get(duoB)
        if current_count == None:
            wins = 0
            games = 0
        games += 1
        if not battle['team_A_wins']:
            wins += 1
        duo_chem[duoB] = (wins,games)
    

with open("2scores.json", "w") as f:
    json.dump(duo_chem, f)
        

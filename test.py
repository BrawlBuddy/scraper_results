import json

result_jsons = ['AD.json', 'AF.json', 'AL.json', 'AS.json', 'DZ.json']

all_merged_results = list()


for file_name in result_jsons:
    with open(file_name, "r") as f:
        temp_result = json.load(f)
        all_merged_results.extend(temp_result)

counter_total = 0 
counter_uneven_teams = 0
greater_counter = 0
less_counter = 0

for battle in all_merged_results:
    if len(battle['team_A']) != 3 or len(battle['team_B']) != 3:
        counter_total += 1
        if len(battle['team_A']) != len(battle['team_B']):
            counter_uneven_teams += 1
        else:
            if len(battle['team_A']) > 3:
                greater_counter += 1
            else:
                less_counter += 1

print(counter_total)
print(counter_uneven_teams)
print(greater_counter)
print(less_counter)
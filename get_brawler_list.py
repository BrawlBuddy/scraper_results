import json

result_jsons = ['AD.json', 'AF.json', 'AL.json', 'AS.json', 'DZ.json']

all_merged_results = list()


for file_name in result_jsons:
    with open(file_name, "r") as f:
        temp_result = json.load(f)
        all_merged_results.extend(temp_result)

brawler_set = set()

for battle in all_merged_results:
    for brawler in battle['team_B']:
        brawler_set.add(brawler)
    for brawler in battle['team_A']:
        brawler_set.add(brawler)


with open("brawler_list.json", "w") as f:
    json.dump(list(brawler_set), f)


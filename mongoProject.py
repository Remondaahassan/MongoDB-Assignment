import json, yaml
from collections import defaultdict 

#open data from file
with open("tim_data.json", "r") as file:
    data = json.load(file)

#initialize data structures
def team_info():
    return{
    "matches_played": 0,
    "climbed_count": 0,
    "total_balls":0,
    "balls":[] 
    }

info = defaultdict(team_info)

for item in data:
    team_num = item["team_num"]
    info[team_num]["matches_played"]+=1
    if item["climbed"]:
        info[team_num]["climbed_count"]+=1
    info[team_num]["total_balls"] +=item["num_balls"]
    info[team_num]["balls"].append(item["num_balls"])


#calculate
results = {}
for team_num, stats in info.items():
    matches_played = stats["matches_played"]
    climbed_count = stats["climbed_count"]
    average_balls = stats["total_balls"]/matches_played if matches_played >0 else 0
    climb_percent = (climbed_count/matches_played)*100 if matches_played>0 else 0
    highest_balls = max(stats["balls"]) if stats["balls"] else 0
    lowest_balls = min(stats["balls"]) if stats["balls"] else 0

    results[team_num] ={
        "matches_played": matches_played,
        "climbed_percent":climb_percent,
        "average_balls": average_balls,
        "highest_balls": highest_balls,
        "lowest_balls": lowest_balls
    }

with open("project_schema.yaml", "r") as yaml_file:
    data_type = yaml.load(yaml_file, yaml.Loader)

for key in stats:
    if str(type(stats[key])) == data_type["team"][key]:
        print("Success")
    else:
        print("Error")

    #put results in a collection
    with open("team_information.json", "w") as file:
        json.dump(results,file, indent = 4)
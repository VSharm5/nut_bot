import json

with open("nut_names.json", 'r') as f:
    names = json.load(f)
    print(names[0])
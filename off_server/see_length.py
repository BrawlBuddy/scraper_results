import json
import os

length = 0

for local_file in os.scandir():
    if local_file.name.split('.')[1] == 'json':
        print(local_file.name)
        with open(local_file.name, "r") as f:
            length += len(json.load(f))

print(length)


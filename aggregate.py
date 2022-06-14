import os   
import json

### file used to create bgm.json

path = "/Users/tunghokang/Desktop/maplebgm-db/bgm" # path to maplebgm-db

final_lst = []
directory = os.fsencode(path)
    
for file in os.listdir(directory):
    file = file.decode("utf-8") 
    if file.endswith(".json"):
        file_path = path+"/"+file
        with open(file_path, 'r') as f:
            data = json.load(f)
            final_lst += data

with open('bgm.json', 'w') as f:
    json.dump(final_lst, f, indent=4)
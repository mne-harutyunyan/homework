import json, yaml

file_name = "data.yaml"
output_file_name = "data.json"
with open(file_name,"r") as fs:
    output = yaml.safe_load(fs)
with open(output_file_name,"x") as fs1:
    json.dump(output,fs1,indent = 2)

import yaml

file_name = "config.yaml"

with open(file_name, "r") as fs:
    file = yaml.safe_load(fs)
    
    if "server" in file and "port" in file["server"]:
        if file["server"]["port"] == 8080:
            file["server"]["port"] = 9090  

with open(file_name, "w") as fs1:
    yaml.safe_dump(file, fs1)

print(file)

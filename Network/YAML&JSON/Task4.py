import json

file_name = "user_data1.json"
output_file_name = 'filtered_users.json'

with open(file_name,"r") as fs:
    file_list = json.load(fs)
    filtered_users = []

    for file in file_list:
        if file['age'] > 30 and file["role"] == "manager":
            filtered_users.append(file)

with open(output_file_name,"a") as fs1:
    json.dump(filtered_users,fs1,indent=2)   


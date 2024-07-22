dict1 = {}
dict2 = {}
dict3 = {}
keys = ['name','surname','ID', 'phone number', 'email', 'password']

for key in keys:
    dict1[key] = input(f"for user 1 enter {key}: ")
for key in keys:
    dict2[key] = input(f"for user 2 enter {key}: ")
for key in keys:
    dict3[key] = input(f"for user 3 enter {key}: ")

#print(dict1)
#print(dict2)
#print(dict3)

list_of_users = []
list_of_users.append(dict1)
list_of_users.append(dict2)
list_of_users.append(dict3)
searched_user = str(input("enter searched user name: "))
for i in range(len(list_of_users)):
    print(f"{i+1} user is {list_of_users[i]}\n")

for i in range(len(list_of_users)):
    if searched_user == str(list_of_users[i]['name']):
        print(list_of_users[i]['name'])
        break
    elif searched_user != str(list_of_users[i]['name']):
        print("Not found")
        break

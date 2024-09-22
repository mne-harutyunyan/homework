# Write a function that reads a JSON file containing a list of dictionaries.
# The function should process the data (e.g., find all entries with a specific attribute) 
# and write the results to a new JSON file.
import json
def process_data(file, new_file, gender):
    file1 = open(file)
    data = json.load(file1)
    file1.close()
    filtered_people = [person for person in data['people'] if person.get('gender') == gender]
    file2 = open(new_file, 'w')
    json.dump({"people": filtered_people}, file2, indent=2)
    file2.close()
    print("success")

process_data("sample.json","new.json","female")

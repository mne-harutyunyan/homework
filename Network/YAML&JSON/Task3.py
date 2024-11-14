import json
file_name = "company_data.json"

company_details = {
  "company": "TechCorp",
  "departments": [
    {
      "name": "Engineering",
      "employees": [
        {"id": 1, "name": "Alice", "role": "Engineer"},
        {"id": 2, "name": "Bob", "role": "Manager"}
      ]
    },
    {
      "name": "Sales",
      "employees": [
        {"id": 3, "name": "Charlie", "role": "Sales Rep"},
        {"id": 4, "name": "Dana", "role": "Sales Lead"}
      ]
    }
  ]
}

with open(file_name,"x") as fs:
    json.dump(company_details,fs, indent = 2)
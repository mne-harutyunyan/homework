# Use the requests module to send a POST request to the URL https://jsonplaceholder.typicode.com/posts.
#  Send JSON data that includes title, body, and userId. Print the response JSON to confirm that
#  the data was posted correctly.
import requests, json

url = "https://jsonplaceholder.typicode.com/posts" 

json_data = "json_data.json"
with open(json_data,"r") as fs:
    data = json.load(fs)
    
response = requests.post(url,json = data)

if response.status_code in [200, 201]:
    print("Response JSON:", response.json())
else:
    print("Failed to post data", response.status_code)
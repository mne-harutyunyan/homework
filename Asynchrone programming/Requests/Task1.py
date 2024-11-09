# Use the requests module to send a GET request to the URL https://jsonplaceholder.typicode.com/posts.
# Retrieve posts by a specific user by adding a query parameter (e.g., ?userId=1). 
# Parse the JSON response and print the titles of the posts.

import requests, json

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId':1}
response = requests.get(url,params)

if response.status_code == 200:
    output = response.json()
    for id in output:
        print(id["title"])
else:
    print(f"Can't retrieve posts... {response.status_code}")



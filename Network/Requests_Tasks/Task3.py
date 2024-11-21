# Write a script to send a GET request to https://jsonplaceholder.typicode.com/invalid-url using the 
# requests module. Implement error handling to catch and print status codes and error messages if the
#  request fails.

import requests
url = 'https://jsonplaceholder.typicode.com/invalid-url'

def test():
    response = requests.get(url)
    if response.status_code ==200:
        print("Response JSON:", response.json())
    else:
        raise Exception(response.status_code)
try:
    test()
except requests.exceptions.RequestException as e:
        print(f"Request failed due to a network error: {e}")
except Exception as e:
    print(f"There is an error: {e}")

# You are building a system to process JSON files that contain user data (such as user profiles or purchase 
# records). Your task is to read multiple JSON files concurrently and extract specific information 
# like user names or purchase totals.
# Use the asyncio library to create coroutines for reading multiple JSON files concurrently.
# Extract specific information from each file (e.g., user names or purchase totals).
# Print the extracted data after all files have been read and processed.
# Use asyncio.gather() to read all files concurrently.

import asyncio, aiofile
import json
file = "user_data.json"

async def read_data(file_path:str)->str:
    print(f'Starting to read the file ... {{{file_path}}}')
    read = open(file_path, mode = "r")
    data = json.load(read)
    user_info = []
    for user in data:
        name = user['name']
        total_amount = sum(purchase['amount'] for purchase in user.get('purchases', []))
        user_info.append({'name': name, 'total_spent': total_amount})

    return user_info


async def main():

    task = read_data(file)

    results = await asyncio.gather(task)

    print(results)


asyncio.run(main())
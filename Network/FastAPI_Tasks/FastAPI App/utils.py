'''This is helper functions module.'''

import json
import os
import aiofiles
import dotenv
dotenv.load_dotenv()

#for environment variables

USERS_FILE = os.environ.get("USERS_FILE")
TASKS_FILE = os.environ.get("TASKS_FILE")
PORT = int(os.environ.get("PORT"))
HOST = os.environ.get("HOST")

#functions for reading and writing JSON files

async def read_file_json(file_name):
    """Read JSON data from a file."""
    try:
        async with aiofiles.open(file_name, 'r') as f:
            content = await f.read()
            return json.loads(content)
    except json.JSONDecodeError:
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps([], indent=2))
        return []
    except FileNotFoundError:
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps([], indent=2))

async def write_file_json(file_name, data):
    """Write JSON data to a file, creating it if it does not exist."""
    try:
        async with aiofiles.open(file_name, 'w') as f:
            await f.write(json.dumps(data, indent=4))
    except json.JSONDecodeError:
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps([], indent=2))
        return []
    except FileNotFoundError:
        async with aiofiles.open(file_name, 'w') as f:
            await f.write(json.dumps([]))
        await write_file_json(file_name, data)
        return []

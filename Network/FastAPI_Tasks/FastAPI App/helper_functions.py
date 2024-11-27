import os,aiofiles, json
from errors import FileError
async def read_file(file_name):
    """Read JSON data from a file."""
    try:
        async with aiofiles.open(file_name, 'r') as f:
            content = await f.read()
            return json.loads(content)
    except json.JSONDecodeError:
        users = []
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps(users, indent=2))
        return users
    except FileNotFoundError:
        users = []
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps(users, indent=2))
        return users
    
async def read_fileT(file_name):
    """Read JSON data from a file."""
    try:
        async with aiofiles.open(file_name, 'r') as f:
            content = await f.read()
            return json.loads(content)
    except json.JSONDecodeError:
        tasks = []
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps(tasks, indent=2))
        return tasks
    except FileNotFoundError:
        tasks = []
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps(tasks, indent=2))
        return tasks
    
async def write_file(file_name, data):
    """Write JSON data to a file."""
    try:
        async with aiofiles.open(file_name, 'w') as f:
            await f.write(json.dumps(data, indent=4))
    except json.JSONDecodeError:
        users = []
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps(users, indent=2))
        return users
    except FileNotFoundError:
        users = []
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps(users, indent=2))
        return users
    except Exception as e:
        raise FileError(f"Error writing {file_name}: {str(e)}")


async def write_fileT(file_name, data):
    """Write JSON data to a file."""
    try:
        async with aiofiles.open(file_name, 'w') as f:
            await f.write(json.dumps(data, indent=4))
    except json.JSONDecodeError:
        tasks = []
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps(tasks, indent=2))
        return tasks
    except FileNotFoundError:
        tasks = []
        async with aiofiles.open(file_name, 'w') as fs:
            await fs.write(json.dumps(tasks, indent=2))
        return tasks
    except Exception as e:
        raise FileError(f"Error writing {file_name}: {str(e)}")



def reader(file_name:str)->str|int:
    if file_name.upper()==("USERS_FILE"):
        USERS_FILE = os.environ.get("USERS_FILE")
        return USERS_FILE
    elif file_name.upper()==("TASKS_FILE"):
        TASKS_FILE = os.environ.get("TASKS_FILE")
        return TASKS_FILE
    elif file_name.upper()==("PORT"):
        PORT = int(os.environ.get("PORT"))
        return PORT
    elif file_name.upper()==("HOST"):
        HOST = os.environ.get("HOST")
        return HOST
    
def is_valid_user(name,email,password)->bool:
    '''Helper function to validate user details.'''
    VALID_DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]

    if name == "":
        return False
    if "@" not in email or email.count("@") != 1:
        return False
    left, right = email.split("@")
    if not left or not right:
        return False
    if right not in VALID_DOMAINS:
        return False
    if "." not in right or right.startswith(".") or right.endswith("."):
        return False  
    if len(password) < 6:
        return False
    if not password.isalnum():
        return False
    return True


def is_valid_task(title,description:str = '')->bool:
    '''Helper function to validate task details.'''
    if title == "":
        return False
    if not isinstance(description,str) or not isinstance(title, str):
        return False
    return True

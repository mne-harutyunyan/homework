import json 
import os
from passlib.context import CryptContext
import time
pwd_context = CryptContext(schemes="sha256_crypt")


def read_data(file_name):
    """Read JSON data from a file."""
    try:
        with open(file_name, 'r') as f:
            content =  f.read()
            return json.loads(content)
    except json.JSONDecodeError:
        with open(file_name, 'w') as fs:
             fs.write(json.dumps({}, indent=2))
        return {}
    except FileNotFoundError:
        with open(file_name, 'w') as fs:
            fs.write(json.dumps({}, indent=2))

def write_data(file_name, data):
    """Write JSON data to a file, creating it if it does not exist."""
    try:
        with open(file_name, 'w') as f:
            f.write(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        with open(file_name, 'w') as fs:
            fs.write(json.dumps({}, indent=2))
        return {}
    except FileNotFoundError:
        with open(file_name, 'w') as f:
            f.write(json.dumps({}))
        write_data(file_name, data)
        return {}

def hash_password(password: str) -> str:
  return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
  return pwd_context.verify(plain_password, hashed_password)

def register_user(username: str, password: str):
  db = read_data("users.json")
  if username in db:
    return False
  db[username] = {"username": username, "password": hash_password(password)}
  write_data("users.json",db)
  return True

def authenticate_user(username: str, password: str) -> bool:
  db = read_data("users.json")
  user = db.get(username)
  if not user:
    return False
  return verify_password(password, user["password"])

def read_data_for_log(file_name):
    """Read JSON data from a file."""
    try:
        with open(file_name, 'r') as f:
            content =  f.read()
            return json.loads(content)
    except json.JSONDecodeError:
        with open(file_name, 'w') as fs:
             fs.write(json.dumps([], indent=2))
        return []
    except FileNotFoundError:
        with open(file_name, 'w') as fs:
            fs.write(json.dumps([], indent=2))

def logger(log:dict):
    logs = read_data_for_log("logs.json")
    logs.append(log)
    try:
        with open("logs.json", 'w') as f:
            f.write(json.dumps(logs, indent=2))
    except json.JSONDecodeError:
        pass

def current_time():
    local_time = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", local_time)
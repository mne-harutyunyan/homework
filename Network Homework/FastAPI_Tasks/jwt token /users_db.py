import json
from passlib.context import CryptContext
from model import User
from config import Config
config = Config()
pwd_context = CryptContext(schemes="sha256_crypt")

def read_file(filepath):
    try:
        with open(filepath) as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}
    
def write_file(filepath,data):
    try:
        with open(filepath, "w") as file:
            return json.dump(data,file, indent=2)
    except json.JSONEncoder:
        return {}
    
def register(username, password):
    users = read_file("users.json")
    if username in users:
        return False
    hashed_password = pwd_context.hash(password)
    users[username] = {"username": username, "password": hashed_password}
    write_file("users.json",users)
    return True

def authenticate_user(username,password):
    users = read_file("users.json")
    current_user = users.get(username)
    if not current_user:
        return False
    return pwd_context.verify(password, current_user["password"])


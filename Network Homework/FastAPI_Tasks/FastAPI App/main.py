'''This is the main module'''

from contextlib import asynccontextmanager
import json
import os
import aiofiles
import dotenv
import uvicorn
from fastapi import FastAPI
from models import User
from models import Task
from errors import NotFoundError, FileError, ValidationError
from utils import read_file_json, write_file_json, USERS_FILE,TASKS_FILE,HOST,PORT

dotenv.load_dotenv()

@asynccontextmanager
async def lifespan(_: FastAPI):
    '''for init'''
    for file_name in [USERS_FILE, TASKS_FILE]:
        if not os.path.exists(file_name) or os.stat(file_name).st_size == 0:
            async with aiofiles.open(file_name, 'w') as f:
                await f.write(json.dumps([]))
    print("Initialization complete.")
    yield
    print("App is shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    '''Welcome function'''
    return "Welcome to our app..."

@app.get("/users")
async def get_users()-> list:
    '''Retrieve a list of all users.'''
    users = await read_file_json(USERS_FILE)
    return users

@app.get("/users/{user_id}")
async def get_user(user_id:int):
    ''' Retrieve a user by ID'''
    users = await read_file_json(USERS_FILE)
    usero = [user for user in users if user_id == int(user["id"])]
    if usero:
        return usero
    else:
        raise NotFoundError("User not found", 404)

@app.post("/users")
async def create_user(user:User):
    '''Add a new user with fields: name, email, password.'''

    users = await read_file_json(USERS_FILE)
    u_id=len(users)+1
    user.id = u_id
    for u in users:
        if user.email == u['email']:
            raise ValidationError("Email is already in use.", 400)
    users.append(user.model_dump())
    await write_file_json(USERS_FILE,users)
    return {"message": "User created successfully", "user": user}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    '''Update an existing user's details by ID.'''

    users = await read_file_json(USERS_FILE)

    for u in users:
        if u["id"] == user_id:
            user.id = user_id
            u.update(user.model_dump())
            await write_file_json(USERS_FILE, users)
            return {"message": f"User {user_id} upated successfully", "user": user}
    raise NotFoundError("User ID not found", 404)

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete a user by ID."""
    users = await read_file_json(USERS_FILE)
    user_to_delete = None

    for user in users:
        if user["id"] == user_id:
            user_to_delete = user
            break

    if user_to_delete:
        users.remove(user_to_delete)
        await write_file_json(USERS_FILE, users)
        return {"message": f"User {user_id} deleted successfully"}

    raise NotFoundError("User ID not found", 404)

@app.get("/tasks")
async def get_tasks()->list:
    '''Retrieve a list of all tasks.'''
    tasks = await read_file_json(TASKS_FILE)
    return tasks

@app.get("/tasks/{task_id}")
async def get_task(task_id:int):
    '''Retrieve a task by ID'''
    tasks = await read_file_json(TASKS_FILE)
    task = [task for task in tasks if task_id == int(task["id"])]
    if task:
        return task
    raise NotFoundError("Task is not found", 404)

@app.post("/tasks")
async def create_task(task: Task):
    '''Add a new task with fields: title, description, and user ID'''

    task_user_id = task.user_id
    description = task.description

    if not task_user_id:
        raise NotFoundError("User ID is required", 404)
    users = await read_file_json(USERS_FILE)
    user_found = False
    for user in users:
        if user['id'] == task_user_id:
            user_found = True
            break
    if not user_found:
        raise FileError("User is not found", 404)
    tasks = await read_file_json(TASKS_FILE)
    task_id = len(tasks) + 1
    task.id = task_id
    if not description:
        task.__dict__.pop("description")
    tasks.append(task.model_dump())
    await write_file_json(TASKS_FILE, tasks)
    return {"message": "Task created successfully", "task_id": task_id}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task by ID."""

    tasks = await read_file_json(TASKS_FILE)
    task_to_delete = None

    for task in tasks:
        if task["id"] == task_id:
            task_to_delete = task
            break

    if task_to_delete:
        tasks.remove(task_to_delete)
        await write_file_json(TASKS_FILE, tasks)
        return {"message": f"Task {task_id} deleted successfully"}

    raise NotFoundError("Task ID not found", 404)


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    '''Update an existing task's details by ID.'''

    tasks = await read_file_json(TASKS_FILE)
    users = await read_file_json(USERS_FILE)
    for u in users:
        if not u['id'] == task.user_id:
            raise NotFoundError("User id is not found", 404)
    for t in tasks:
        if t["id"] == task_id:
            task.id = task_id
            t.update(task.model_dump())
            await write_file_json(TASKS_FILE, tasks)
            return {"message": f"Task {task_id} upated successfully", "task": task}
    raise NotFoundError("Task ID not found", 404)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True,host=HOST,port=PORT)

from fastapi import FastAPI, HTTPException
import uvicorn, dotenv
import json 
from errors import ValidationError, NotFoundError, FileError
from helper_functions import reader, is_valid_user,is_valid_task ,read_file, write_file,read_fileT,write_fileT

dotenv.load_dotenv()
app = FastAPI()
    
@app.get("/users")
async def get_user():
    '''Retrieve a list of all users.'''
    try:
        users = await read_file(reader("USERS_FILE")) 
        return users
    except Exception as e:
        raise FileError(f"File is not found: {str(e)}")

@app.post("/users/register")
async def create_user(user:dict):
    '''Add a new user with fields: name, email, password.'''
    name = user.get("name")
    email = user.get("email")
    password = user.get("password")

    try:
        users = await read_file(reader("USERS_FILE")) 
        max_id = max([u['id'] + 1 for u in users]) if users else 1
    except Exception:
            users = []
            max_id = 1

    if not is_valid_user(name,email,password):
        raise ValidationError(status_code=400,message="Enter valid vaules for name , email and password...")
    for u in users:
        if u["email"] == email:
            raise ValidationError(status_code=400,message="Email already exists.")
    else:
        new_user = {"id":max_id,"name":name,"email":email, "password":password}
        users.append(new_user)
        new_users = await write_file(reader("USERS_FILE"),users)
        return {"message":f"{name} added to users list successfully",
                "user":{
                    "id": max_id,
                    "name": name,
                    "email": email}
                }
@app.get("/users/login")
async def login_user(user:dict,name="Name"):
    '''Function for logging in'''
    email = user.get("email")
    password = user.get("password")
    if not is_valid_user(name,email,password):
        raise ValidationError("Invalid email or password", 401)
    else:
        try:
            users = await read_file(reader("USERS_FILE"))
        except FileNotFoundError:
            raise FileError("File is not found", 404)
    for user in users:
        if user["email"]==email and user["password"]==password:
            return {"message":"Login successful",
                    "user":{
                    "id": user["id"],
                    "name": user["name"],
                    "email": user['email']}
                    }
        else:
            return "Invalid email or password. If you don't have an account, please register first."
        
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """Retrieve a specific user by ID."""
    try:
        users = await read_file(reader("USERS_FILE")) 
        for user in users:
            if int(user["id"]) == int(user_id):
                return {"user": user}
        raise NotFoundError(status_code=404, message="User is not found.")           
    except NotFoundError:
        raise NotFoundError("User is not found.",404)
    except json.JSONDecodeError:
        users = []
        new_users = await write_file(reader("USERS_FILE"),users)

@app.put("/users/{user_id}")
async def update_user(updated_user:dict,user_id: int):
    '''Update an existing user's details by ID.'''
    name = updated_user.get("name")
    email = updated_user.get("email")
    password = updated_user.get("password")
    if not is_valid_user(name,email, password):
        raise ValidationError(status_code=400,message="Enter valid values for name , email and password...")
    try:
        users = await read_file(reader("USERS_FILE")) 
        if any(user["email"] == email and int(user["id"]) != user_id for user in users):
            raise ValidationError(status_code=400,message="Email already exists..")
        for user in users:
            if int(user["id"]) == int(user_id):
                user['name']=name
                user['email']=email
                user['password']=password
                break
        else:   
            raise NotFoundError(status_code=404, message="User is not found.")           
    except Exception:
        raise FileError("File is not found", 404)
    try:
        new_users = await write_file(reader("USERS_FILE"),users)
        return f"{user_id} updated: {name} added to users list successfully."
    except Exception:
        raise FileError("File is not found", 404)

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete a user by ID"""
    try:
        users = await read_file(reader("USERS_FILE"))
        for user in users:
            if int(user["id"]) == int(user_id):
                users.remove(user)
                break
        else:
            raise NotFoundError(status_code=404, message="User is not found.")           
    except Exception:
        raise FileError("File is not found", 404)
    try:
        new_users = await write_file(reader("USERS_FILE"),users)
        return f'{user["name"]} removed successfully'
    except Exception:
        raise FileError("File is not found", 404)

@app.post("/tasks")
async def create_task(task:dict):
    title = task.get("title")
    description = task.get("description")
    user_id = task.get("user_id")

    if not is_valid_task(title, description):
        raise HTTPException(status_code=400,detail="Enter valid task details...")
    try:
        users = await read_file(reader("USERS_FILE"))
    except FileNotFoundError:
        FileError("File is not found")
    try:
        tasks = await read_fileT(reader("TASKS_FILE")) 
        max_id = max([t['id'] + 1 for t in tasks]) if tasks else 1
    except Exception:
            tasks = []
            max_id = 1

    if not any(int(user["id"]) == user_id for user in users):
        raise HTTPException(status_code=404, detail="User ID not found.")
    else:
        new_task = {"id":max_id, "title":title,"description":description,"user_id":user_id}
    tasks.append(new_task)
    new_tasks = await write_fileT(reader("TASKS_FILE"),tasks )
    return {"Message": f''' {new_task['title']}:Task was added to User{user_id}'s tasks.''',
            "Task":new_task
            }

@app.get("/tasks")
async def get_task():
    '''Retrieve a list of all tasks.'''
    try:
        tasks = await read_fileT(reader("TASKS_FILE"))
        return tasks
    except Exception:
        raise FileError("File is not found", 404)

@app.get("/tasks/{task_id}", status_code=200)
async def get_task(task_id: int):
    """Retrieve a specific task by ID."""
    try:
        tasks = await read_fileT(reader("TASKS_FILE")) 
        for task in tasks:
            if int(task["id"]) == int(task_id):
                return {"task": task}
        raise NotFoundError(status_code=404, message="Task is not found.")           
    except NotFoundError:
        raise NotFoundError("Task is not found.",404)
    except json.JSONDecodeError:
        tasks = []
        new_tasks = await write_fileT(reader("TASKS_FILE"),tasks)

@app.put("/tasks/{task_id}")
async def update_task(updated_task:dict,task_id: int):
    '''Update an existing task's details by ID.'''
    title = updated_task.get("title")
    description = updated_task.get("description")
    user_id = updated_task.get("user_id")
    if not is_valid_task(title,description):
        raise ValidationError(status_code=400,message="Enter valid values for title and description...")
    try:
        users = await read_file(reader("USERS_FILE"))
    except FileNotFoundError:
        FileError("File is not found")
    if not any(int(user["id"]) == user_id for user in users):
        raise HTTPException(status_code=404, detail="Task ID is not found.")
    else:
        tasks = await read_fileT(reader("TASKS_FILE"))
        for task in tasks:
            if int(task["id"]) == int(task_id):
                task['title']=title
                task['description']=description
                task['user_id']=user_id
                break
        else:   
            raise NotFoundError(status_code=404, message="Task is not found.")           
    
    try:
        new_tasks = await write_fileT(reader("TASKS_FILE"),tasks)
        return f"Task{task_id} updated: {title} added to tasks list successfully."
    except Exception:
        raise FileError("File is not found", 404)

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task by ID"""
    try:
        tasks = await read_fileT(reader("TASKS_FILE"))
        for task in tasks:
            if int(task["id"]) == int(task_id):
                tasks.remove(task)
                break
        else:
            raise NotFoundError(status_code=404, message="Task is not found.")           
    except Exception:
        raise FileError("File is not found", 404)
    try:
        new_tasks = await write_fileT(reader("TASKS_FILE"),tasks)
        return f'{task["title"]} removed successfully'
    except Exception:
        raise FileError("File is not found", 404)


if __name__ == "__main__":
    uvicorn.run("main:app",port = reader("PORT"), host = reader("HOST"), reload = True)


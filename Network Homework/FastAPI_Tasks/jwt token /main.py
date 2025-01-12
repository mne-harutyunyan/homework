from fastapi import FastAPI, Request, status, HTTPException, Response, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from config import Config
from fastapi.security import OAuth2PasswordBearer
from model import User
from users_db import register , authenticate_user
from auth import create_jwt_token,verify_jwt_token

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

config = Config()

@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    return "Welcome to our app..."

@app.get("/register", response_class=HTMLResponse)
async def registration(request:Request):
    return "This is the registration page..."

@app.post("/register", response_class=HTMLResponse)
async def register_user(request:Request, user:User):
    if not register(user.username, user.password):
        raise HTTPException(400,"Username already exists")
    return "Successfully registrated"

@app.post("/login")
async def login_user(user: User):
    if not authenticate_user(user.username, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    auth_token = create_jwt_token({"sub": user.username})
    return {"auth_token": auth_token}

@app.get("/secure")
async def secure_page(request: Request, token: str=Depends(oauth2_scheme)):
  username = verify_jwt_token(token)
  return {"request": request, "username": username}

if __name__ == "__main__":
    uvicorn.run("main:app",port=config.PORT, reload= True)

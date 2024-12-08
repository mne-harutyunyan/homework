import os
import dotenv
import uvicorn
from fastapi import FastAPI, Request, Response, status, Depends, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models import User
from auth import register, login, sessions, authenticate

dotenv.load_dotenv()
PORT = int(os.environ.get("PORT"))
template = os.environ.get("TEMPLATES_PATH")
templates = Jinja2Templates(directory=template)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
  return templates.TemplateResponse('login.html', {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def regiser(request: Request):
  return templates.TemplateResponse('register.html', {"request": request})

@app.post("/register")
async def register_user_form(user:User):
  register(user.username,user.password)
  return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)

@app.post("/login")
async def login_user(user:User):
    return login(user.username, user.password)

def get_current_username(username: str = Cookie(None)):
    return authenticate(username)

@app.get("/secure")
async def secure_page(request: Request, username: str=Depends(get_current_username)):
  if username not in sessions:
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
  return templates.TemplateResponse("secure.html", {"request": request, "username": username})

@app.get("/logout")
def logout_user(response: Response):
  RedirectResponse(url="/", status_code=status.HTTP_301_MOVED_PERMANENTLY)
  response.delete_cookie('username')

if __name__ == '__main__':
  uvicorn.run('main:app', port=PORT, reload=True)
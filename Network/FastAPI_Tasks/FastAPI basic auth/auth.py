
from users_db import register_user,logger,current_time, authenticate_user
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse

sessions={}

def register(username,password):
    if not register_user(username,password):
        log = {"event":"register", "username": username,"status": "failed","time":current_time()}
        logger(log)
        raise HTTPException(status_code=400, detail='Username already exist')
    log = {"event":"register", "username": username,"status": "succeed","time":current_time()}
    logger(log)

def login(username,password):
    if not authenticate_user(username, password):
        log = {"event":"login", "username": username,"status": "failed","time":current_time()}
        logger(log)
        raise HTTPException(status_code=401, detail="Invalid credentials")
    sessions[username] = True
    log = {"event":"login", "username": username,"status": "succeed","time":current_time()}
    logger(log)
    redirect_response = RedirectResponse(url='/secure', status_code=status.HTTP_303_SEE_OTHER)
    redirect_response.set_cookie(key="username", value=username)
    return redirect_response

def authenticate(username):
    if not username:
        log = {"event":"secure", "username": username,"status": "failed","time":current_time()}
        logger(log)
        raise HTTPException(status_code=401, detail = "Not authenticated")
    log = {"event":"secure_page_access", "username": username,"status": "succeed","time":current_time()}
    logger(log)
    return username
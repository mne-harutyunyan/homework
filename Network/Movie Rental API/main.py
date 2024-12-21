import uvicorn
from fastapi import FastAPI
from utils.config import config
from routers import auth, movies, rentals
from database.database import engine, Base


app = FastAPI(title="Movie Rental API",version='1.0.0',
              description='FastAPI project that simulates a simple movie rental system')
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(rentals.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload = True, port = config.port)

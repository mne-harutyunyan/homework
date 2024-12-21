from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from models import schemas
from models.models import Movie,User
from routers.auth import get_current_user
from database.database import get_db
router = APIRouter(prefix='/movies',tags=['Movies'])


@router.get("/", response_model=list[schemas.Movie])
def get_movies(db: Session = Depends(get_db)):
    '''Function to get all movies'''
    return db.query(Movie).all()

@router.post("/")
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    '''Function to create a movie'''
    db_movie = db.query(Movie).filter(Movie.title == movie.title).first()
    if db_movie:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Movie already exists")
    db_movie = Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return {'user':current_user.username, 'movie':db_movie}

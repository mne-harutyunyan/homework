from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.auth import get_current_user
from models import schemas
from models.models import Rental, Movie, User
from database.database import get_db

router = APIRouter(prefix="/rentals",tags=['Rentals'])

@router.post("/", response_model=schemas.Rental)
def rent_movie(rental: schemas.RentalCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    '''Function to rent a movie'''
    db_movie = db.query(Movie).filter(Movie.id == rental.movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    db_rental = Rental(user_id=current_user.id, movie_id=rental.movie_id,
                       rental_duration=rental.rental_duration)
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental

@router.get("/", response_model=list[schemas.Rental])
def get_rentals(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    '''Function to get rentals of user'''
    return db.query(Rental).filter(Rental.user_id == current_user.id).all()

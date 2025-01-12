from pydantic import BaseModel, Field,EmailStr

class UserCreate(BaseModel):
    username: str = Field(...,min_length=2, max_length=50)
    password: str = Field(...,min_length=2, max_length=50)
    email: EmailStr

class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

class MovieCreate(BaseModel):
    title: str = Field(...,min_length=2, max_length=50)
    genre: str
    rating: int = Field(...,gt=0,le=10)

class Movie(MovieCreate):
    id: int

    class Config:
        from_attributes = True

class RentalCreate(BaseModel):
    movie_id: int
    rental_duration: int

class Rental(RentalCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True

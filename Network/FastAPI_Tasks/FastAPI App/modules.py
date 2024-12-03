'''This is modul for models'''
from typing import Optional
from pydantic import BaseModel,EmailStr,Field

class User(BaseModel):
    '''Represents a user in the system.'''
    id:Optional[int] = None
    name:str = Field(...,min_length=2,max_length=35)
    email:EmailStr
    password:str = Field(...,min_length=6)

class Task(BaseModel):
    '''Represents a task in the system.'''
    id:Optional[int] = None
    title:str = Field(...,max_length=35,min_length=2)
    description:Optional[str]=None
    user_id:int

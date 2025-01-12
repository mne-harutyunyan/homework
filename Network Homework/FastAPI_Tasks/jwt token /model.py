from pydantic import BaseModel, Field

class User(BaseModel):
    username:str = Field(..., min_length = 2)
    password:str = Field(..., min_length = 2, max_length=50)
    
    
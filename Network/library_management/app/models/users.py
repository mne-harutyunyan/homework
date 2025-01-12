from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
  username: str
  email: str
  password: str
  is_active: bool = True

class UserIn(BaseModel):
  email: EmailStr
  password: str

class UserOut(UserBase):
  id: str
  username: str

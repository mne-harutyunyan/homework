from fastapi import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from app.helpers.config import settings
from app.helpers.validation import validate_password, validate_email
from app.models.users import UserBase, UserIn
from app.services.user_service import create_user, sign_in_user, update_existing_user

router = APIRouter(prefix='/users', tags=['Users'])
db_client = AsyncIOMotorClient(settings.MONGO_URI)
db = db_client.library

@router.post('/signup')
async def signup(user: UserBase):
  validate_password(user.password)
  validate_email(user.email)
  await create_user(user)
  return {"message": "User registered successfully"}

@router.post('/signin')
async def signin(user: UserIn):
  token = await sign_in_user(user)
  return {"access_token": token, "token_type": "bearer"}

@router.put('/{id}')
async def update_user(user_id: str, user: UserBase):
  validate_password(user.password) and validate_email(user.email)
  await update_existing_user(user_id,user)
  return {"message": " User updated successfully"}

import os
from typing import Optional
import dotenv

dotenv.load_dotenv()

class Config:
    '''For managing environment variables configuration'''
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.init_env()
        return cls.__instance

    def __init__(self):
        self.port = None
        self.jwt_secret_key = None
        self.database_url = None

    def init_env(self):
        self.port = self.get_env("PORT", cast=int)
        self.jwt_secret_key = self.get_env("JWT_SECRET_KEY")
        self.database_url = self.get_env("DATABASE_URL")

    def get_env(self, key: str, cast: Optional[type] = None):
        value = os.environ.get(key)
        if not value:
            raise ValueError(f"env does not have specified key: {key}")
        if cast is not None:
            return cast(value)
        return value
config = Config()
config.init_env()

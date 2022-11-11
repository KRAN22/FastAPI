from fastapi import FastAPI ,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from tortoise import fields
from    
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id : str
    username : str
    password_hash : str 

    @classmethod
    async def get_user(cls,username):
        return cls.get(username==username)

    def verify_password(self,password):
        return True
    
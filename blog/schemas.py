from pydantic import BaseModel,Field
from typing import Optional



class Blog(BaseModel):
    title: str
    body: str

class User(BaseModel):
    
    Name: str
    Age: int
       
class Person(BaseModel):
    
    name : str
    password : str
    email: str
    
    class Config:
        orm_mode = True
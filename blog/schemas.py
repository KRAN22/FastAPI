from pydantic import BaseModel,Field
from typing import Optional



class Blog(BaseModel):
    id : int
    title: str
    body: str

class User(BaseModel):
    
    id:Optional[int] = Field(default=None, primary_key=True)
    Name: str
    Age: int
    
    class Config:
        orm_mode = True
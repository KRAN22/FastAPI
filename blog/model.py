from sqlalchemy import String, Integer,Column
from .database import Base

class Blog(Base):
    __tablename__ = "Blogs"
    
    id = Column(Integer,primary_key=True,index= True)
    title = Column(String)
    body = Column(String)
    
    
class User(Base):
    __tablename__ = "User"
    
    id = Column(Integer,primary_key=True,index= True)
    Name = Column(String(255))
    Age = Column(Integer)
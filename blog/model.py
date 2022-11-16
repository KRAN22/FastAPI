from sqlalchemy import String, Integer,Column
from .database import Base

class Blog(Base):
    __tablename__ = "Blogs"
    
    id = Column(Integer,primary_key=True,index= True)
    title = Column(String)
    body = Column(String)
    
    
class Blogs(Base):
    __tablename__ = "User"
    
    id = Column(Integer,primary_key=True,index= True)
    title = Column(String)
    body = Column(String)
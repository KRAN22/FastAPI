from sqlalchemy import String, Integer,Column
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "Blogs"
    
    id = Column(Integer,primary_key=True,autoincrement=True,index= True)
    title = Column(String)
    body = Column(String)
    
    creator = relationship("User", back_populates="blogs")
    
    
class User(Base):
    __tablename__ = "User"
    
    id = Column(Integer,primary_key=True,index= True,autoincrement=True)
    Name = Column(String(255))
    Age = Column(Integer)
    
    blogs = relationship("Blog", back_populates="creator")
    
    
class Person(Base):
    __tablename__ = "Persons"
    
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))   
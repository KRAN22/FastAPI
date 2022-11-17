from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import model
from .database import engine,SessionLocal
from sqlalchemy.orm import Session

class Blog:
    def create_blog(blog,db):
        print('create blog inside api')
        #create model to save in db 
        new_blog = model.Blog(title=blog.title,body=blog.body)
        #save to db
        db.add(new_blog)
        db.commit()
        print('successfully create blog')
        return blog

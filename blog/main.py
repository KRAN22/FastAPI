from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas,model
from .database import engine,SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

#1-Create API
'''
@app.post("/blog")
def create_blog(blog: schemas.Blog):
    return blog
'''
#2-Logic
# Blog - Method
@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog,  db:Session = Depends(get_db) ):
    print('create blog inside api')
    #create model to save in db 
    new_blog = model.Blog(title=blog.title,body=blog.body)
    #save to db
    db.add(new_blog)
    db.commit()
    print('successfully create blog')
    return blog

@app.get("/blog")
def get_blog(db:Session = Depends(get_db)):
    print("Enter into db....")
    blog = db.query(model.Blog).all() 
    return blog

# User - Methods

@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User,  db:Session = Depends(get_db) ):
    print('create blog inside api')
    #create model to save in db 
    new_user = model.User(id = user.id,Name=user.Name,Age=user.Age)
    #save to db
    db.add(new_user)
    db.commit()
    print('successfully create blog')
    return user







# @app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def destroyBlog(id:int,db:Session = Depends(get_db)):
#     db.query(model.Blog).filter(model.Blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return "Done Deleting...."

# @app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
# def updateBlog(id:int,db:Session = Depends(get_db)):
#     db.query(model.Blog).filter()

# @app.get("/blog")
# def get_blog(db:Session = Depends(get_db)):
#     blogs = db.query(model.Blog).all()
#     return blogs

# @app.get("/blog/{id}",status_code=200)
# def get_blog_by_id(id: int,response:Response ,db:Session = Depends(get_db)):
#     blog = db.query(model.Blog).filter(model.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )
#     return blog
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
def create_user(user: schemas.User, response : Response, db:Session = Depends(get_db) ):
    print('create blog inside api')
    #create model to save in db 
    new_user = model.User(id = user.id,Name=user.Name,Age=user.Age)
    all_user = db.query(model.User).all()
    for u in all_user:
        if u.id == new_user.id:
            response.status_code = status.HTTP_208_ALREADY_REPORTED
            raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail=f"This id {new_user.id} already exists")
    #save to db
    db.add(new_user)
    db.commit()
    print('successfully create blog')
    return user

@app.get("/user")
def get_user(db:Session=Depends(get_db)):
    print("Enter inti DB.......")
    user = db.query(model.User).all()
    return user

@app.get("/user/{id}",status_code=status.HTTP_200_OK)
def get_user_by_id(id : int , db:Session=Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"user with the id {id} is not available" )
    return user 
    
    
@app.delete("/user/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroyUser(id : int ,db:Session = Depends(get_db)):   
    db.query(model.User).filter(model.User.id).delete(synchronize_session=False)
    db.commit()
    return "Done Deleting...."
        

@app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id:int, request : schemas.User, db:Session = Depends(get_db)):
    db.query(model.User).filter(model.User.id == id).update(request,synchronize_session=False)
    db.commit()
    return "Updated...."
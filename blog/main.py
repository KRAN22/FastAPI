from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas,model
from .database import engine,SessionLocal
from sqlalchemy.orm import Session

from .blog import Blog

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
def create_blog(blog: schemas.Blog, db:Session = Depends(get_db)):
    blogs = Blog().create_blog(blog, db)
    print(blogs)
    return blogs


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
    new_user = model.User(Name=user.Name,Age=user.Age)
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
    user = db.query(model.User).filter(model.User.id == id)
    if not user.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"user with the id {id} is not available" )
    
    user.delete()
    db.commit()
    return "Done Deleting...."
        

@app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id:int, request : schemas.User, db:Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id)
    if not user.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"user with the id {id} is not available" )
    user.update(request)
    db.commit()
    return "Updated...."

@app.post("/person",status_code=status.HTTP_201_CREATED)
def createPerson(request : schemas.Person,db : Session= Depends(get_db)):
    print('create blog inside api')
    new_person = model.Person(name = request.name ,password = request.password,email= request.email)
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    print('successfully create blog')
    return new_person
    
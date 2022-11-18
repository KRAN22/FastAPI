from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas,model
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash

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
@app.post("/blog", status_code=status.HTTP_201_CREATED,tags=["Blogs"])
def create_blog(blog: schemas.Blog, db:Session = Depends(get_db)):
    blogs = Blog.create_blog(blog, db)
    return blogs


@app.get("/blog",tags=["Blogs"])
def get_blog(db:Session = Depends(get_db)):
    print("Enter into db....")
    blog = db.query(model.Blog).all() 
    return blog

# User - Methods

@app.post("/user", status_code=status.HTTP_201_CREATED,tags=["user"])
def create_user(user: schemas.User, response : Response, db:Session = Depends(get_db) ):
    print('create blog inside api')
    #create model to save in db 
    new_user = model.User(Name=user.Name,Age=user.Age)
    #save to db
    db.add(new_user)
    db.commit()
    print('successfully create blog')
    return user

@app.get("/user",tags=["user"])
def get_user(db:Session=Depends(get_db)):
    print("Enter inti DB.......")
    user = db.query(model.User).all()
    return user

@app.get("/user/{id}",status_code=status.HTTP_200_OK,tags=["user"])
def get_user_by_id(id : int , db:Session=Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"user with the id {id} is not available" )
    return user 
    
    
@app.delete("/user/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["user"])
def destroyUser(id : int ,db:Session = Depends(get_db)):   
    user = db.query(model.User).filter(model.User.id == id)
    if not user.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"user with the id {id} is not available" )
    
    user.delete()
    db.commit()
    return "Done Deleting...."
        

@app.put("/user/{id}",status_code=status.HTTP_202_ACCEPTED,tags=["user"])
def updateUser(id:int, request : schemas.User, db:Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id)
    if not user.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"user with the id {id} is not available" )
    user.update(request)
    db.commit()
    return "Updated...."


# persons curd operations

@app.post("/person",response_model= schemas.ShowPerson, status_code=status.HTTP_201_CREATED,tags=["Person"])
def createPerson(request : schemas.Person,db : Session= Depends(get_db)):
    print('create blog inside api')
    new_person = model.Person(name = request.name ,password = Hash.bcrypt(request.password),email= request.email)
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    print('successfully create blog')
    return new_person
    
@app.get("/person/{id}",response_model=schemas.ShowPerson,tags=["Person"])
def get_person(id: int,db : Session= Depends(get_db)):
    person = db.query(model.Person).filter(model.Person.id == id).first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with this id {id} is not available") 
    return person

@app.delete("/person/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["Person"])
def destroyPerson(id : int ,db:Session = Depends(get_db)):   
    user = db.query(model.Person).filter(model.Person.id == id)
    if not user.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"user with the id {id} is not available" )
    
    user.delete()
    db.commit()
    return "Done Deleting...."
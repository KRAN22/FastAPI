from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/blog")
def index(limit=10,published: bool=True,sort:Optional[str]=None):
    # only get 10 published blogs
    if published:
        return {"data":f'{limit} published blogs from the Database'}
    else:
        return {"data":f'{limit} blogs from the Database'}


@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id     
    return {"Data":id}

@app.get("/blog/{id}/comments")
def comments(id):
    #fetch comments of blog with id = id
    return {"Data":{"1","2"}}

class Blog(BaseModel):
    title : str
    Body : str
    Published : Optional[bool]


@app.post('/blog')
def create_blog(request :Blog):
    return {"data":f"Blog is created with title as {request.title}"}
students={
    1:{
        "name" : "Kranthi",
        "Age" : 23,
        "year" : "5th",
    },
    2:{
        "name" : "ramya",
        "Age" : 20,
        "year" : "7th",
    }
}

@app.get("/get_students")
def get_students():
    return students

@app.get("/get_students/{student_id}")
def get_students(student_id: int = Path(None,description = "the ID  of the student you want to view",gt=0,lt=4)):
    return students[student_id]

@app.get("/get_by_name/{student_id}")
def get_students(*,student_id:int, name : Optional[str] = None,test : int = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "data not found"}

class Student(BaseModel):
    name : str
    Age : int
    year : str 

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    Age : Optional[int] = None
    year : Optional[str] = None

@app.post("/create_students/{student_id}")
def create_students(student_id:int,student:Student):
    if student_id in students:
        return {"Error":"Student already exists"}
    students[student_id]=student
    return students[student_id]

@app.put("/updateStudent{student_id}")
def updateStudent(student_id: int,student : UpdateStudent):
    if student_id not in students:
        return {"Error":"Students does not exist"}
    # students[student_id] = student
    if student.name != None:
        students[student_id].name = student.name
    if student.Age != None:
        students[student_id].Age = student.Age 
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/deleteStudent/{student_id}")
def deleteStudent(student_id:int):
    if student_id not in students:
        return{"Error": "Students does not exist"}
    del students[student_id]
    return {"Msg":"Student deleted successfully"}




# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)
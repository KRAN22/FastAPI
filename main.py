from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data":{"name":"kranthi"}}


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


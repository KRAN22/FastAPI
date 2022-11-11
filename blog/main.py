from fastapi import FastAPI
from . import schemas,model
from .database import engine


app = FastAPI()

model.Base.metadata.create_all(engine)

@app.post("/blog")
def create(request:schemas.Blog):
    return request


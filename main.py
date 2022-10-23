from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data":{"name":"kranthi"}}

@app.get("/about")
def about():
    return {"Data":"About Page"}
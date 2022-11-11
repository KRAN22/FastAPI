from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app = FastAPI()

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def token(form_data:OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username + "token"}


@app.get("/")
def index(token:str = Depends(oauth2_schema)):
    return {"the_token": token }
     



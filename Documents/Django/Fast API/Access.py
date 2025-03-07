from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class ATAI(BaseModel):
    username: str
    password: str  
@app.post("/AI/", response_model=ATAI)
async def AI(nu: str = Form(...), pwd: str = Form(...)):
    return ATAI(username=nu, password=pwd)

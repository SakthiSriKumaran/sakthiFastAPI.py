from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Rectangle(BaseModel):
    w: int
    h: int

app = FastAPI(title="Area of the Rectangle")
@app.get("/wel")

def welcome():
    return {"Welcome to Area of Rectangle Formula"}

@app.post("/start")
def area(r: Rectangle): 
    return {"area_of_rectangle": r.h * r.w}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

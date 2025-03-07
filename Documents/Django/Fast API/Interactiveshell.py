from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

class Sakthi(BaseModel):
    id: int
    name: str
    subject: List[str] = []


data = {
    'id': 129,
    'name': 'sakthi',
    'subject': ['python', 'flask', 'FastAPI']
}

s1 = Sakthi(**data)  

print(s1)
app = FastAPI()

#@app.get("/root")
#def read_root():
#   return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

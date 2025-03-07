from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

class Sakthi(BaseModel):
    id: int
    name: str = Field(None, title="Hi FastAPI", max_length=20)
    marks: List[int] = []

@app.post("/sakthi12/")
def sakthi1():
    data = {
        'id': 129,
        'name': 'sakthi',
        'marks': [129, 58, 59]
    }

    s1 = Sakthi(**data)

    print(s1)
    print(type(s1))  

    return s1 

@app.post("/sakthi129/")
async def read_vari():
    print("Hello World")    

if __name__ == "__main__":
   uvicorn.run(app, host="127.0.0.1", port=8000, reload="True")

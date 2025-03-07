from typing import List,Tuple,Dict
from fastapi import FastAPI
app=FastAPI(
    title="FastAPI is python based framework",
    version="1.0.0",
    do="for API development fater"
)
@app.get("/list")
async def List():
    list1= ["chennai","bangalore","hyderbad"]
    # print(List[str]())
    return{list1}
    if list1:
        print("Successfully")
    else:
        print("Failed")
        
@app.get("/dict")

async def Dict():
    Dict={
    "sakthi":"129",
    "Company":"ATAI"
}
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app=FastAPI()

@app.get("/cookie/")

async def create_cookie():
    content={"message":"hi Welcome"}
    response=JSONResponse(content=content)
    response.set_cookie(key="username",value="admin")
    return response

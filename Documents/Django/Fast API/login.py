from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
#from fastapi.staticfiles import StaticFiles

app=FastAPI()

templates=Jinja2Templates(directory="templates")
#app.mount("/static",StaticFiles(directory="static",name="static"))

@app.get("/login/{token}",response_class=HTMLResponse)

async def Login(request:Request,token:int):
    
    return templates.TemplateResponse("login.html",{"request":request,"token":token})
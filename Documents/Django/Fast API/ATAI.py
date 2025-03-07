from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



app=FastAPI()

templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/ATAI/{name}",response_class=HTMLResponse)

async def Maari(request:Request,name:str):
    return templates.TemplateResponse("ATAI.html",{"request":request,"name":name})
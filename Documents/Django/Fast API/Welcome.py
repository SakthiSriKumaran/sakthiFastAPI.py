from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request

app = FastAPI() 

templates = Jinja2Templates(directory="templates")

@app.get("/welcome", response_class=HTMLResponse)
async def sakthi(request: Request):
    return templates.TemplateResponse("Hello.html", {"request": request,"name" : "sakthi"})

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/company/{name}", response_class=HTMLResponse)

async def company(request: Request, name: str):
    return templates.TemplateResponse("hi.html", {"request": request, "name": name})

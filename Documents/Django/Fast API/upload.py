from fastapi import FastAPI,File,UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import uvicorn
app=FastAPI()

templates=Jinja2Templates(directory="templates")

@app.get("/upload/",response_class=HTMLResponse)

async def Upload(request:Request):
    return templates.TemplateResponse("upload.html",{"request":request})


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000,reload="True")

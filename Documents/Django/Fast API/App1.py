from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app=FastAPI()
@app.get("/HTML",response_class=HTMLResponse)

async def Hello():
    content_HTML="""
    <html>
    <body bgcolor="lightgreen">
    <p> Hi Sakthi </p>
    </body>
    </html>
    """
    return HTMLResponse(content=content_HTML)

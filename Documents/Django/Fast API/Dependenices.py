from fastapi import FastAPI, Depends
import uvicorn

class Sakthi:
    def __init__(self):
        self.message = "Hello Welcome to ATAI"
    
    def get_read(self):
        return self.message

app = FastAPI()

def get_service() -> Sakthi:
    return Sakthi()

@app.get("/message")
def get_out(sakthi: Sakthi = Depends(get_service)):
    return {"message": sakthi.get_read()}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

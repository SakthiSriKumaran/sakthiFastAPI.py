import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/app")
def read_uvi(Token_no: int = 129):
    return {"Token_No": Token_no}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.0", port=8000, reload=True)
    
if uvicorn.run(True):
    print("Successfully")
else:
    print("Failed")

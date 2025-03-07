from fastapi import FastAPI

class Employee:
    def __init__(self, name: str = "sakthi"):
        self.name = name


employee = Employee(name="ATAI Employee")


app = FastAPI(title="Employee of the ATAI")

@app.get("/initial")
def read():
    return {"Name of the Person": employee.name}   

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)




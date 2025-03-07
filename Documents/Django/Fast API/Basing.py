from fastapi import FastAPI

app = FastAPI(title="this is Typing the variable")

@app.get("/hello")
async def hello(name: str, age: int):
    return {"hello ATAI Company": {"name": name, "age": age}}

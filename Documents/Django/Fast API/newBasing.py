from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/world/{name}/{age}")
def world(
    name: str = Path(..., min_length=10, max_length=20),
    age: int = Path(..., gt=3, le=20)
):
    return {"message": "Hello World", "name": name, "age": age}

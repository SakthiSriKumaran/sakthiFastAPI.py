from fastapi import FastAPI
app=FastAPI()

@app.get("/12")
def root():
    return '<p>mari</p>'
@app.get("/sakthi")
def read_root(token_no=129):
    return{"token_no": token_no}


@app.get("/print")
def read_print():
    print("hello world")  
    return {"message": "Printed hello world to console"}

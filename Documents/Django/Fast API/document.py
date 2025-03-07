from fastapi import FastAPI
app=FastAPI(
    title="FastAPI is python based framework",
    version="1.0.0",
    do="for API development fater"
)
@app.get("/")

def read_Doc(token_no:int=129,Tname:str="sakthi"):
    return{"Token_no":token_no,"Trainee_name":Tname}
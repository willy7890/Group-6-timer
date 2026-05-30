# from fastapi import FastAPI
# app = FastAPI()
# @app.post("/")
# def read_root():
#     return {"message": "Welcome to Filoteo's API!"}

from fastapi import FastAPI
app = FastAPI()
@app.get("/hello")
async def hello(name:str, age:int):
    return {"name": name, "age":age}
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
# # def division(a: int, b: int):
#     if b == 0:
#         return {"error": "Denominator cannot be zero"}
#     return {"result": a / b}
# def say_hello(name):
#     return {"message": f"Hello, {name}!"}
# def say_hello(name: str):
#     return  "Hello" "+" +name 
# async def __init__(enter,w: int, h: int):
#     enter.width = w
#     enter.height = h
#     async def area(rectangle):
#         return rectangle.width * rectangle.height
#     # print("area= ", await area(enter))    
async def hello(name,age):
    return {"name": name, "age": age}
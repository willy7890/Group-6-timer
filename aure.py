from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def jina():
    return {"message" : "Hello world"}
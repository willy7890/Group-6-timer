from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime
app = FastAPI()
diary=[]
class DiaryEntry(BaseModel):
    title: str
    date: date
    content: str
@app.post("/diary")
def home():
    return {"message": "Welcome to mgs diary"}
@app.post("/write")
def write_diary(entry: DiaryEntry):
    diary_entry = {
        "date":
datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "title":entry.title,
            "content":entry.content 
        }

    diary.append(diary_entry)
    return {
        "message":"diary entry saved",
           "entry":diary_entry
           }         
@app.get("/entries")
def get_entries():
    return diary

@app.get("/entry/{entry_id}")
def get_entry(entry_id:int):
    if entry_id < len(diary):
        return diary[entry_id]
    return{"error":"Entry not found"}

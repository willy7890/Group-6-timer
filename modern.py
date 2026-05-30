from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app=FastAPI(
    title="task flow API",
    description="Modern task management"
)
task=[]
class Task(BaseModel):   
 title: str
 description: str

@app.get("/")
def home():
 return {"message":"welcome to the modern task flow.", "time": datetime.now()}

@app.post("/task")
def create_task(task: Task):
    task_dict = task.dict()
    task.append(task_dict)
    return {"message": "Task created successfully", "task": task_dict}  
@app.get("/tasks")
def get_task():
  return task
@app.get("/task/{task_id}")
def get_task_by_id(task_id: int):
    if task_id < len(task):
        return task[task_id]
    else:
        return {"message": "Task not found"}

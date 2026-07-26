from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="AI Task API", version="1.0")

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

tasks_storage = [
    {"id": 1, "title": "Set up development environment", "done": True},
    {"id": 2, "title": "Build FastAPI endpoints", "done": False},
    {"id": 3, "title": "Complete Stage 7 AI rematch", "done": False},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-generated Task API"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_storage

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_id = max([t["id"] for t in tasks_storage], default=0) + 1
    new_task = {"id": new_id, "title": task.title, "done": False}
    tasks_storage.append(new_task)
    return new_task
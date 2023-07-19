from typing import Union
from fastapi import FastAPI, status, HTTPException
import sqlite3
from dataclient import DataClient
app = FastAPI() 
dataclient = DataClient()





@app.get("/")
def read_root():
    return {
        "info": "This is simple todo app for managing your daily tasks",
        "tasks_list": "/tasks"
        }

@app.get("/tasks/")
def read_tasks():
    return dataclient.getTasks()

@app.get("/tasks/{task_id}")
def read_task(task_id: int, q = None):
    result = dataclient.getTask(task_id)

    if (result == None):
        raise HTTPException(status_code=404, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")
    else:
        return result

@app.post("/tasks/")
def create_task(task: dict):
    taskid = task.get('id')
    tasktitle = task.get('title')
    taskcompleted = task.get('completed')
    return dataclient.createtask(taskid, tasktitle,taskcompleted)
    # return "Received"

@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_task:dict):
    tasktitle = new_task.get('title')
    taskcompleted = new_task.get('completed')
    dataclient.updateTask(task_id, tasktitle, taskcompleted)
    

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = dataclient.getTasks()
    for task in tasks:
        if(task["id"] == task_id):
            dataclient.deletetask(task_id)
            break
    else:  
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")
    
    return task_id


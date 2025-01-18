from fastapi import FastAPI
from celery.result import AsyncResult
from tasks import celery_app, detect_persons

app = FastAPI()

@app.post("/detect/")
async def detect(image_url: str):
    task = detect_persons.delay(image_url)
    return {"task_id": task.id, "status": "Task submitted"}

@app.get("/task-status/{task_id}")
async def task_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)

    if result.state == "PENDING":
        return {"task_id": task_id, "status": "PENDING", "message": "Task is waiting to execute."}
    elif result.state == "SUCCESS":
        return {"task_id": task_id, "status": "SUCCESS", "result": result.result}
    elif result.state == "FAILURE":
        return {"task_id": task_id, "status": "FAILURE", "error": str(result.traceback)}
    else:
        return {"task_id": task_id, "status": result.state}

import requests
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from celery import Celery
import multiprocessing
import os
from ultralytics import YOLO
import redis
import uuid
import cv2
import numpy as np

multiprocessing.set_start_method('spawn')
app = FastAPI()

# Configure Redis and Celery
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
celery_app = Celery(
    'task',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

model = YOLO(r'./models/yolov8n.pt')

def detect_persons(image):
    """Detect persons in the image using OpenCV."""
    if image is None or image.size == 0:
        raise HTTPException(status_code=404, detail="Image is empty")
    print("[INFO] original image shape: " + str(image.shape) + "image dtype: " + str(image.dtype))
    image = cv2.resize(image, (300, 300))
    print("[INFO] original image shape: " + str(image.shape) + "image dtype: " + str(image.dtype))

    results = model.predict(source=image, save=False, conf=0.5, classes=[0])
    annotated_image = results[0].plot()

    detections = results[0].boxes.data.cpu().numpy()
    count = len(detections)

    return count, annotated_image

@celery_app.task
def process_image_task(image_data):
    """Celery task to process image data."""
    nparr = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    count, processed_image = detect_persons(image)
    filename = f"output_{uuid.uuid4().hex}.jpg"
    # cv2.imwrite(filename, processed_image)

    result = f'Task ID: {process_image_task.request.id}, Count: {count}, Processed Image: {filename}\n'
    results_path = os.path.join(os.getcwd(), 'output', 'results.txt')
    os.makedirs(os.path.dirname(results_path), exist_ok=True)

    with open(results_path, "a") as file:
        file.write(result)

    return {'count': count, 'output_file': filename}

@app.post("/detect/from_disk")
async def detect_from_disk(filepath: str):
    """Endpoint to detect persons from a local image file."""
    try:
        with open(filepath, 'rb') as f:
            image_data = f.read()
        task = process_image_task.apply_async(args=[image_data])
        return JSONResponse(content={'task_id': task.id}, status_code=202)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/detect/from_url")
async def detect_from_url(image_url: str):
    """Endpoint to detect persons from an image URL."""
    try:
        response = requests.get(image_url)
        image_data = response.content
        task = process_image_task.apply_async(args=[image_data])
        return JSONResponse(content={'task_id': task.id}, status_code=202)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/detect/from_upload")
async def detect_from_upload(file: UploadFile = File(...)):
    """Endpoint to detect persons from an uploaded image file."""
    try:
        image_data = await file.read()
        task = process_image_task.apply_async(args=[image_data])
        return JSONResponse(content={'task_id': task.id}, status_code=202)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/task/status/{task_id}")
async def get_task_status(task_id: str):
    """Endpoint to check the status of a task."""
    task = process_image_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        return JSONResponse(content={'status': 'PENDING'}, status_code=202)
    elif task.state == 'SUCCESS':
        return JSONResponse(content={'status': 'SUCCESS', 'result': task.result}, status_code=200)
    else:
        return JSONResponse(content={'status': task.state}, status_code=500)

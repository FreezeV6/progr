from ultralytics import YOLO
import requests
import tempfile
import os
from celery import Celery

# Initialize Celery
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

# Load the YOLOv8 model from the local file
MODEL_PATH = "./models/yolov8n.pt"
model = YOLO(MODEL_PATH)

@celery_app.task
def detect_persons(image_url: str):
    try:
        # Fetch the image
        response = requests.get(image_url, stream=True)
        if response.status_code != 200:
            return {"error": f"Failed to fetch the image from {image_url}"}

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name

        # Perform detection
        results = model.predict(source=temp_file_path, save=False, conf=0.4, classes=[0])  # Class 0 is "person"

        # Count persons detected
        persons_detected = len(results[0].boxes)
        os.remove(temp_file_path)

        return {"persons_detected": persons_detected, "url": image_url}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

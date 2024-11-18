import csv
import uuid
from datetime import datetime


def add_task(file_name='tasks.csv'):
    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "status": "pending",
        "timestamp": datetime.now().isoformat()
    }

    try:
        with open(file_name, 'x', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=task.keys())
            writer.writeheader()
    except FileExistsError:
        pass

    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=task.keys())
        writer.writerow(task)
    print(f"Added task: {task_id}")


if __name__ == "__main__":
    add_task()

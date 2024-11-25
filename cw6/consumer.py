import csv
import time
import os


def consume_tasks(file_name='tasks.csv', lock_file='tasks.lock'):
    while True:
        if not os.path.exists(file_name):
            print("No tasks file found. Waiting...")
            time.sleep(5)
            continue

        tasks = []
        pending_tasks = []

        if os.path.exists(lock_file):
            print("File is locked by another process. Retrying...")
            time.sleep(2)
            continue
        try:
            open(lock_file, 'w').close()

            with open(file_name, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    tasks.append(row)
                    if row["status"] == "pending":
                        pending_tasks.append(row)
        finally:
            if os.path.exists(lock_file):
                os.remove(lock_file)

        if pending_tasks:
            task_to_process = pending_tasks[0]
            print(f"Consuming task {task_to_process['id']}")

            for task in tasks:
                if task["id"] == task_to_process["id"]:
                    task["status"] = "in_progress"

            try:
                open(lock_file, 'w').close()
                with open(file_name, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=tasks[0].keys())
                    writer.writeheader()
                    writer.writerows(tasks)
            finally:
                if os.path.exists(lock_file):
                    os.remove(lock_file)

            time.sleep(30)

            for task in tasks:
                if task["id"] == task_to_process["id"]:
                    task["status"] = "done"

            try:
                open(lock_file, 'w').close()
                with open(file_name, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=tasks[0].keys())
                    writer.writeheader()
                    writer.writerows(tasks)
            finally:
                if os.path.exists(lock_file):
                    os.remove(lock_file)

            print(f"Task {task_to_process['id']} is done.")
        else:
            print("No pending tasks. Waiting...")
            time.sleep(5)


if __name__ == "__main__":
    consume_tasks()

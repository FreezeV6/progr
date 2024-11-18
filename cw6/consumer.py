import csv
import time
import os
from datetime import datetime


def consume_tasks(file_name='tasks.csv', lock_file='tasks.lock'):
    while True:
        # Sprawdź, czy plik istnieje
        if not os.path.exists(file_name):
            print("No tasks file found. Waiting...")
            time.sleep(5)
            continue

        # Odczytujemy zadania z pliku
        tasks = []
        pending_tasks = []

        # Tworzymy blokadę pliku
        if os.path.exists(lock_file):
            print("File is locked by another process. Retrying...")
            time.sleep(2)
            continue
        try:
            # Tworzymy blokadę
            open(lock_file, 'w').close()

            with open(file_name, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    tasks.append(row)
                    if row["status"] == "pending":
                        pending_tasks.append(row)
        finally:
            # Usuwamy blokadę
            if os.path.exists(lock_file):
                os.remove(lock_file)

        # Sprawdzamy, czy są zadania do wykonania
        if pending_tasks:
            task_to_process = pending_tasks[0]  # Pobieramy pierwsze zadanie z kolejki
            print(f"Consuming task {task_to_process['id']}")

            # Aktualizujemy status na "in_progress"
            for task in tasks:
                if task["id"] == task_to_process["id"]:
                    task["status"] = "in_progress"

            # Zapisujemy status "in_progress" z blokadą
            try:
                open(lock_file, 'w').close()
                with open(file_name, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=tasks[0].keys())
                    writer.writeheader()
                    writer.writerows(tasks)
            finally:
                if os.path.exists(lock_file):
                    os.remove(lock_file)

            # Symulujemy wykonywanie zadania
            time.sleep(30)

            # Aktualizujemy status na "done"
            for task in tasks:
                if task["id"] == task_to_process["id"]:
                    task["status"] = "done"

            # Zapisujemy status "done" z blokadą
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

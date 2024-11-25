import sqlite3
from datetime import datetime
import uuid

DB_FILE = 'tasks.db'

def initialize_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                status TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_task():
    task_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()
    status = "pending"

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (id, status, timestamp)
            VALUES (?, ?, ?)
        ''', (task_id, status, timestamp))
        conn.commit()
        print(f"Added task: {task_id}")

if __name__ == "__main__":
    initialize_db()
    add_task()

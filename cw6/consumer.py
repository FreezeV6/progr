import sqlite3
import time
from datetime import datetime

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

def consume_tasks():
    while True:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id, timestamp FROM tasks
                WHERE status = "pending"
                ORDER BY timestamp ASC
                LIMIT 1
            ''')
            task = cursor.fetchone()

            if task:
                task_id, timestamp = task
                print(f"Consuming task {task_id}")

                cursor.execute('''
                    UPDATE tasks
                    SET status = "in_progress"
                    WHERE id = ?
                ''', (task_id,))
                conn.commit()

                time.sleep(30)

                cursor.execute('''
                    UPDATE tasks
                    SET status = "done"
                    WHERE id = ?
                ''', (task_id,))
                conn.commit()
                print(f"Task {task_id} is done.")
            else:
                print("No pending tasks. Waiting...")
                time.sleep(5)

if __name__ == "__main__":
    initialize_db()
    consume_tasks()

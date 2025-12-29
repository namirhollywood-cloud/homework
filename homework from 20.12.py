import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

TASKS_FILE = "tasks.txt"

tasks = []
next_id = 1


def load_tasks():
    global tasks, next_id
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = f.read()
            if data:
                tasks = json.loads(data)
                if tasks:
                    next_id = max(task["id"] for task in tasks) + 1


def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        f.write(json.dumps(tasks))


class TodoHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == "/tasks":
            self.send_json(tasks)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        global next_id

        if self.path == "/tasks":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)

            task = {
                "id": next_id,
                "title": data["title"],
                "priority": data["priority"],
                "isDone": False
            }

            tasks.append(task)
            next_id += 1
            save_tasks()

            self.send_json(task)

        elif self.path.startswith("/tasks/") and self.path.endswith("/complete"):
            parts = self.path.split("/")
            try:
                task_id = int(parts[2])
            except:
                self.send_response(404)
                self.end_headers()
                return

            for task in tasks:
                if task["id"] == task_id:
                    task["isDone"] = True
                    save_tasks()
                    self.send_response(200)
                    self.end_headers()
                    return

            self.send_response(404)
            self.end_headers()

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    load_tasks()
    server = HTTPServer(("localhost", 8000), TodoHandler)
    print("Server started on http://localhost:8000")
    server.serve_forever()

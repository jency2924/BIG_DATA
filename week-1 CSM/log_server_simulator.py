"""
log_server_simulator.py
------------------------
Pretends to be 3 College Management System servers
(Student, Examination, Library).

Each server acts as a TCP server and continuously sends
College Management log records to the Log Harvester.

Run this FIRST and keep it running.
"""

import socket
import threading
import random
import time
from datetime import datetime

# Simulated College Management servers
DEPARTMENTS = [
    ("student-management", 9001),
    ("examination", 9002),
    ("library", 9003),
]

LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]

# Sample log messages
MESSAGE_TEMPLATES = {
    "INFO": [
        "Student ID {id} registered successfully",
        "Student ID {id} profile updated",
        "Attendance marked for Student ID {id}",
        "Library book issued to Student ID {id}",
        "Exam fee paid by Student ID {id}",
    ],

    "WARNING": [
        "Attendance below 75% for Student ID {id}",
        "Library book due date approaching for Student ID {id}",
        "Exam hall ticket not downloaded by Student ID {id}",
    ],

    "ERROR": [
        "Admission failed for Student ID {id}",
        "Database connection lost while updating marks",
        "Exam result generation failed",
        "Library transaction failed for Student ID {id}",
    ],

    "DEBUG": [
        "Fetching student record ID {id}",
        "Database query executed for Student ID {id}",
        "Cache refreshed for Student ID {id}",
    ],
}


def build_log_line(department):
    """Generate one College Management log line."""

    level = random.choice(LEVELS)
    student_id = random.randint(1001, 9999)

    message = random.choice(
        MESSAGE_TEMPLATES[level]
    ).format(id=student_id)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"{timestamp} | {level} | {department} | {message}\n"


def handle_client(connection, department):

    print(f"[{department}] Harvester Connected")

    try:
        while True:

            log = build_log_line(department)

            connection.sendall(log.encode("utf-8"))

            time.sleep(random.uniform(0.10, 0.50))

            # Send invalid record occasionally
            if random.random() < 0.05:
                connection.sendall(b"INVALID_LOG_RECORD\n")

    except (BrokenPipeError, ConnectionResetError):
        print(f"[{department}] Harvester Disconnected")

    finally:
        connection.close()


def run_department_server(department, port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(("127.0.0.1", port))

    server.listen(1)

    print(f"{department} Server Running on Port {port}")

    while True:

        connection, address = server.accept()

        threading.Thread(
            target=handle_client,
            args=(connection, department),
            daemon=True
        ).start()


if __name__ == "__main__":

    print("\nCollege Management System Log Server Started\n")

    threads = []

    for department, port in DEPARTMENTS:

        t = threading.Thread(
            target=run_department_server,
            args=(department, port),
            daemon=True
        )

        t.start()

        threads.append(t)

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nServer Stopped Successfully.")
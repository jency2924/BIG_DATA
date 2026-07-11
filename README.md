# College Management System - Log Harvester

## Project Overview

The College Management System Log Harvester is a Python-based project that simulates real-time log generation from multiple college departments. The system collects, validates, partitions, stores, and retrieves log data efficiently using TCP socket programming and binary file storage.

This project demonstrates concepts such as high-velocity log processing, multithreading, binary encoding/decoding, and log partitioning, making it suitable as a Big Data mini project.

---

## Features

- Simulates multiple college department servers.
- Streams logs continuously using TCP sockets.
- Uses multithreading for concurrent log collection.
- Validates log format using Regular Expressions.
- Stores logs in compact binary (.bin) files.
- Partitions logs by Department and Log Level.
- Reads binary files and converts them back into human-readable logs.
- Displays processing statistics in real time.

---

## Project Structure

```
College_Management_System/
│
├── log_server_simulator.py
├── log_harvester_daemon_college_management.py
├── read_binary_logs.py
├── print_simple.py
├── partitions/
│     ├── student-management_INFO.bin
│     ├── examination_ERROR.bin
│     ├── library_WARNING.bin
│     └── ...
└── README.md
```

---

## Modules

### 1. log_server_simulator.py

Simulates multiple College Management department servers.

Departments:
- Student Management
- Examination
- Library

Each server continuously generates log records such as:

- Student Registration
- Attendance
- Examination
- Library Transactions

---

### 2. log_harvester_daemon_college_management.py

Acts as the Log Harvester.

Responsibilities:

- Connects to all department servers.
- Receives log streams.
- Validates log format.
- Rejects invalid logs.
- Encodes records into binary format.
- Stores logs inside partition files.
- Displays live processing statistics.

---

### 3. read_binary_logs.py

Reads binary partition files.

Functions:

- Decodes binary records.
- Displays timestamp.
- Displays log level.
- Displays department.
- Displays log message.

---

## Technologies Used

- Python 3
- Socket Programming
- Multithreading
- Regular Expressions (Regex)
- Binary File Handling
- Struct Module
- TCP/IP Networking

---

## Log Format

```
YYYY-MM-DD HH:MM:SS | LEVEL | Department | Message
```

Example:

```
2026-07-11 10:15:21 | INFO | student-management | Student ID 1023 registered successfully
```

---

## Binary Record Format

Each log is stored as:

```
Record Length
Timestamp
Log Level
Department Length
Department Name
Message Length
Message
```

This format reduces storage size while preserving all log information.

---

## How to Run

### Step 1

Start the log server simulator.

```
python log_server_simulator.py
```

---

### Step 2

Open another terminal and start the Log Harvester.

```
python log_harvester_daemon_college_management.py
```

---

### Step 3

After binary files are created inside the **partitions** folder, read any partition file.

Example:

```
python read_binary_logs.py partitions/student-management_INFO.bin
```

---

## Sample Output

```
College Management System Logs

Timestamp  : 2026-07-11 10:15:21
Level      : INFO
Department : student-management
Message    : Student ID 1056 registered successfully
```

---

## Learning Outcomes

This project demonstrates:

- TCP Socket Programming
- Multithreading
- Binary Data Encoding
- Binary Data Decoding
- Regular Expression Validation
- Log Partitioning
- File Handling
- High Velocity Data Processing
- Big Data Log Collection Concepts

---

## Future Enhancements

- MySQL Database Integration
- Hadoop HDFS Storage
- Apache Kafka Integration
- Spark Streaming
- Web Dashboard
- Real-time Analytics
- Log Search Interface
- User Authentication

---

## Developed By

**Maria Jency**

BCA Student

College Management System - Big Data Mini Project

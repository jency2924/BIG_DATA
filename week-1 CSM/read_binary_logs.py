"""
read_binary_logs.py
--------------------
Reads a binary partition file and decodes it into human-readable
College Management System log records.

This program proves that the generated .bin files contain
structured and recoverable log data.

Usage:
    python read_binary_logs.py partitions/college-admission_ERROR.bin
"""

import struct
import sys

# Log level mapping
LEVEL_CODE = {
    "DEBUG": 0,
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3
}

CODE_LEVEL = {v: k for k, v in LEVEL_CODE.items()}


def read_records(filepath):
    """
    Read all binary log records from the given partition file.
    """

    with open(filepath, "rb") as file:
        data = file.read()

    offset = 0
    records = []

    while offset < len(data):

        # Read record length (4 bytes)
        (record_length,) = struct.unpack_from("!I", data, offset)
        offset += 4

        # Extract one complete record
        record = data[offset:offset + record_length]
        offset += record_length

        # Decode:
        # Timestamp (19 bytes)
        # Level (1 byte)
        # Service length (2 bytes)

        timestamp_bytes, level_code, service_length = struct.unpack_from(
            "!19sBH",
            record,
            0
        )

        position = 22

        # Department / Module name
        service = record[position:position + service_length].decode("utf-8")
        position += service_length

        # Message length
        (message_length,) = struct.unpack_from("!H", record, position)
        position += 2

        # Log message
        message = record[position:position + message_length].decode("utf-8")

        records.append({
            "timestamp": timestamp_bytes.decode("ascii").strip(),
            "level": CODE_LEVEL[level_code],
            "department": service,
            "message": message
        })

    return records


def display_records(records):
    """
    Display decoded College Management logs.
    """

    print("\n========== College Management System Logs ==========\n")

    for index, record in enumerate(records, start=1):
        print(f"Record {index}")
        print("-" * 45)
        print(f"Timestamp  : {record['timestamp']}")
        print(f"Log Level  : {record['level']}")
        print(f"Department : {record['department']}")
        print(f"Message    : {record['message']}")
        print()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python read_binary_logs.py <path-to-bin-file>")
        sys.exit(1)

    file_path = sys.argv[1]

    records = read_records(file_path)

    print(f"\nSuccessfully decoded {len(records)} log records from:")
    print(file_path)

    display_records(records)
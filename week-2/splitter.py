import os

def split_file():
    # Input file name
    input_file = "input.txt"

    # Create chunks folder if it doesn't exist
    os.makedirs("chunks", exist_ok=True)

    # Read all lines
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Find middle of file
    mid = len(lines) // 2

    # Split into two chunks
    chunk1 = lines[:mid]
    chunk2 = lines[mid:]

    # Write Chunk 1
    with open("chunks/chunk1.txt", "w") as file:
        file.writelines(chunk1)

    # Write Chunk 2
    with open("chunks/chunk2.txt", "w") as file:
        file.writelines(chunk2)

    print("Input file split successfully!")

if __name__ == "__main__":
    split_file()
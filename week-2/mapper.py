import os

def run_mapper():

    os.makedirs("partitions", exist_ok=True)

    chunk_files = ["chunks/chunk1.txt", "chunks/chunk2.txt"]

    output_file = "partitions/mapped.txt"

    with open(output_file, "w") as out:

        for chunk in chunk_files:

            with open(chunk, "r") as file:

                for line in file:
                    word = line.strip()

                    if word:
                        out.write(f"{word}\t1\n")

    print("Mapper completed successfully!")


if __name__ == "__main__":
    run_mapper()
from collections import defaultdict
import os

def run_reducer():

    os.makedirs("output", exist_ok=True)

    word_count = defaultdict(int)

    files = [
        "partitions/partition0.txt",
        "partitions/partition1.txt"
    ]

    for filename in files:

        with open(filename, "r") as file:

            for line in file:
                word, count = line.strip().split("\t")
                word_count[word] += int(count)

    with open("output/result.txt", "w") as out:

        for word in sorted(word_count):
            out.write(f"{word}\t{word_count[word]}\n")

    print("Reducer completed successfully!")


if __name__ == "__main__":
    run_reducer()
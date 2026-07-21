import os

def partition_data():

    input_file = "partitions/mapped.txt"

    partition0 = "partitions/partition0.txt"
    partition1 = "partitions/partition1.txt"

    with open(input_file, "r") as file, \
         open(partition0, "w") as p0, \
         open(partition1, "w") as p1:

        for line in file:
            word, count = line.strip().split("\t")

            if word[0].lower() < "n":
                p0.write(line)
            else:
                p1.write(line)

    print("Partitioning completed successfully!")


if __name__ == "__main__":
    partition_data()
def sort_partitions():

    files = [
        "partitions/partition0.txt",
        "partitions/partition1.txt"
    ]

    for filename in files:

        with open(filename, "r") as file:
            lines = file.readlines()

        lines.sort()

        with open(filename, "w") as file:
            file.writelines(lines)

    print("Sorting completed successfully!")


if __name__ == "__main__":
    sort_partitions()
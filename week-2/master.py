import splitter
import mapper
import partitioner
import sorter
import reducer

def main():
    print("========== MapReduce Engine ==========")

    print("Step 1: Splitting input file...")
    splitter.split_file()

    print("Step 2: Running Mapper...")
    mapper.run_mapper()

    print("Step 3: Partitioning data...")
    partitioner.partition_data()

    print("Step 4: Sorting partitions...")
    sorter.sort_partitions()

    print("Step 5: Running Reducer...")
    reducer.run_reducer()

    print("=====================================")
    print("MapReduce Job Completed Successfully!")

if __name__ == "__main__":
    main()
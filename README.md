#week-1

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


#week-2

MapReduce Engine Simulation using Python

## Project Title
MapReduce Engine Simulation using Python

## Objective
The objective of this project is to understand the working of the MapReduce framework by implementing a simple MapReduce engine using Python. The project demonstrates data splitting, mapping, partitioning, sorting, and reducing operations.

## Project Structure

week-2/
│
├── master.py
├── splitter.py
├── mapper.py
├── partitioner.py
├── sorter.py
├── reducer.py
├── input.txt
│
├── chunks/
│   ├── chunk1.txt
│   └── chunk2.txt
│
├── partitions/
│   ├── mapped.txt
│   ├── partition0.txt
│   └── partition1.txt
│
└── output/
    └── result.txt

## Modules

### master.py
Controls the complete execution of the MapReduce process.

### splitter.py
Splits the input file into two chunks.

### mapper.py
Reads the chunks and converts each word into (word, 1) key-value pairs.

### partitioner.py
Partitions the mapped data into different files.

### sorter.py
Sorts all key-value pairs alphabetically.

### reducer.py
Counts the occurrences of each word and generates the final output.

## Input

Apple
Orange
Apple
Banana
Apple
Orange
Banana
Apple
Mango
Banana

## Output

Apple    4
Banana   3
Mango    1
Orange   2

## Software Requirements

- Python 3.13 or above
- Visual Studio Code
- Windows 10/11

## Steps to Run

1. Open the project in VS Code.
2. Ensure all Python files are present.
3. Place the input data in input.txt.
4. Run master.py.
5. Check the final output in output/result.txt.

## Learning Outcomes

- Understood the MapReduce workflow.
- Learned file handling in Python.
- Implemented Mapper and Reducer concepts.
- Simulated distributed data processing.

## Conclusion

The MapReduce Engine Simulation project successfully demonstrates the working principles of the MapReduce programming model. The implementation performs data splitting, mapping, partitioning, sorting, and reducing to generate the final word count output.





# Mini Spark RDD Framework using Python

A lightweight implementation of Apache Spark's core concepts using Python. This project demonstrates how **RDD (Resilient Distributed Dataset)** operations, **DAG (Directed Acyclic Graph)** execution, and **lazy evaluation** work internally.

---

## 📌 Project Overview

This project simulates a simplified Spark execution engine capable of:

- Loading CSV datasets
- Creating RDD objects
- Applying lazy transformations
- Building an execution DAG
- Optimizing the DAG
- Executing transformations
- Displaying final results

The sample application filters Amazon product data and returns highly rated Electronics products.

---

## 🚀 Features

- CSV Data Loading
- RDD Abstraction
- Lazy Evaluation
- Directed Acyclic Graph (DAG)
- Map Transformation
- Filter Transformation
- FlatMap Transformation
- Collect Action
- Count Action
- Simple DAG Optimizer
- Execution Engine

---

## 📂 Project Structure

```
Project/
│
├── Data/
│   └── amazon.csv
│
├── src/
│   ├── __init__.py
│   ├── dag.py
│   ├── executor.py
│   ├── loader.py
│   ├── node.py
│   ├── optimizer.py
│   ├── parser.py
│   ├── rdd.py
│   └── utils.py
│
├── main.py
└── README.md
```

---

## ⚙️ How It Works

### Step 1
Load the Amazon dataset from CSV.

### Step 2
Create an RDD object.

### Step 3
Apply transformations.

- Filter Electronics products
- Filter products with rating > 4
- Map product names

### Step 4
Build an execution DAG.

### Step 5
Optimize the DAG.

### Step 6
Execute the pipeline.

### Step 7
Display final results.

---

## 🔄 Execution Flow

```
CSV Dataset
      │
      ▼
Load CSV
      │
      ▼
Create RDD
      │
      ▼
Filter
      │
      ▼
Filter
      │
      ▼
Map
      │
      ▼
Build DAG
      │
      ▼
Optimizer
      │
      ▼
Executor
      │
      ▼
Collect()
      │
      ▼
Display Result
```

---

## 🧩 Supported Transformations

| Transformation | Description |
|---------------|-------------|
| map() | Transforms each record |
| filter() | Filters records based on a condition |
| flatMap() | Expands one record into multiple records |

---

## ⚡ Supported Actions

| Action | Description |
|--------|-------------|
| collect() | Executes the DAG and returns all results |
| count() | Returns the total number of records |

---

## 📊 Sample Pipeline

```python
result = (
    amazon_rdd
        .filter(lambda x: "Electronics" in x["category"])
        .filter(lambda x: float(x["rating"]) > 4)
        .map(lambda x: x["product_name"])
        .collect()
)
```

---

## 🛠 Technologies Used

- Python 3.x
- CSV Module
- Functional Programming
- Object-Oriented Programming (OOP)
- Directed Acyclic Graph (DAG)

---

## 📚 Learning Objectives

This project helps understand:

- Apache Spark Architecture
- RDD Concepts
- Lazy Evaluation
- DAG Execution
- Functional Programming
- Data Processing Pipelines

---

## ▶️ How to Run

Clone the repository.

```bash
git clone <repository-url>
```

Move into the project directory.

```bash
cd Project
```

Run the application.

```bash
python main.py
```

---

## 📌 Example Output

```
Before Execution:

Execution DAG

↓ FILTER
↓ FILTER
↓ MAP

Optimizer Running...

Final Result

Product A
Product B
Product C
...
```

---

## 🔮 Future Improvements

- Reduce Transformation
- GroupBy
- ReduceByKey
- Join Operation
- Parallel Processing
- Multi-threaded Execution
- DAG Optimization Rules
- Partition Support
- Fault Tolerance
- Caching Mechanism

---

## 👨‍💻 Author

**Maria Jency**

Bachelor of Computer Applications (BCA)









## NWE  TASK START


Big Data Analytics – Superstore Sales Analysis
Project Overview

This project performs exploratory data analysis (EDA) on the Sample Superstore dataset using Python. The analysis includes data loading, preprocessing, descriptive statistics, feature engineering, and visualization to understand sales performance across different product categories.

Objectives
Load and explore the Superstore dataset.
Perform data cleaning and preprocessing.
Analyze sales data using descriptive statistics.
Calculate delivery time for each order.
Visualize category-wise sales.
Understand the distribution of sales.

Technologies Used
Python
Google Colab
Pandas
NumPy
Matplotlib
Seaborn
Dataset

Dataset: samplesuperstore.csv

The dataset contains information about:

Order Date
Ship Date
Category
Sales
Customer Details
Product Details
Shipping Information
Steps Performed
1. Import Libraries

Imported the required Python libraries:

Pandas
NumPy
Matplotlib
Seaborn
2. Load Dataset

Loaded the Superstore dataset into a Pandas DataFrame.

3. Data Exploration
Displayed first five records
Checked dataset information
Generated descriptive statistics
4. Data Preprocessing
Converted Order Date and Ship Date into datetime format.
Created a new column:
Delivery Days = Ship Date − Order Date
5. Data Validation
Checked missing values.
Displayed unique product categories.
6. Data Analysis

Calculated total sales for each product category using GroupBy.

7. Data Visualization

Generated:

Bar Chart showing Sales by Category
Histogram showing Sales Distribution
Output

The project provides:

Dataset summary
Missing value analysis
Delivery days calculation
Category-wise total sales
Sales distribution visualization
Learning Outcomes

After completing this project, you will be able to:

Work with real-world datasets.
Perform data preprocessing.
Apply exploratory data analysis (EDA).
Create meaningful visualizations.
Extract business insights from sales data.
Future Enhancements
Regional sales analysis
Profit analysis
Customer segmentation
Monthly and yearly sales trends
Interactive dashboard using Power BI or Tableau
Conclusion

This project demonstrates the fundamentals of Big Data Analytics using Python by analyzing the Sample Superstore dataset. It helps understand sales patterns, delivery performance, and category-wise business insights through statistical analysis and visualizations.



# Task 2 – Big Data Analysis

## 📌 Project Overview

This project focuses on performing **data analysis and exploratory data visualization** using the **Sample Superstore dataset**.

The main objective is to understand sales, profit, discount, delivery time, category-wise performance, and relationships between numerical variables using Python and popular data analysis libraries.

## 🎯 Objectives

* Load and inspect the Superstore dataset.
* Perform basic data preprocessing.
* Convert date columns into proper datetime format.
* Calculate delivery time in days.
* Check for missing values.
* Analyze sales and profit by category.
* Study the distribution of sales and profit.
* Analyze the relationship between discount and profit.
* Generate a correlation matrix and heatmap.
* Visualize important business insights using graphs.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Google Colab
* Jupyter Notebook

## 📂 Dataset

**Dataset:** Sample Superstore Dataset

The dataset contains business transaction information such as:

* Order Date
* Ship Date
* Category
* Sales
* Profit
* Discount
* Other numerical and categorical attributes

## 🔄 Data Preprocessing

The following preprocessing steps were performed:

1. Imported the required Python libraries.
2. Loaded the CSV dataset using Pandas.
3. Inspected the dataset using `df.info()` and `df.describe()`.
4. Converted **Order Date** and **Ship Date** into datetime format.
5. Calculated **Delivery Days** using the difference between shipping and order dates.
6. Checked unique values in the Category column.
7. Checked for missing values.

## 📊 Exploratory Data Analysis

### 1. Sales by Category

Total sales were calculated by grouping the data based on **Category**.

A bar chart was used to visualize the total sales for each category.

### 2. Sales Distribution

A histogram was created to understand the distribution of sales values across the dataset.

### 3. Profit by Category

A bar plot was created to compare profit across different product categories.

### 4. Sales Distribution by Category

A category-wise bar plot was used to visualize sales across different categories.

### 5. Profit Distribution

A box plot was used to study the overall distribution and variation of profit.

### 6. Profit Variation Across Categories

A category-wise box plot was created to understand the variation of profit between categories.

### 7. Impact of Discount on Profit

A scatter plot was used to analyze the relationship between **Discount** and **Profit**.

### 8. Correlation Analysis

Numerical columns were selected and a correlation matrix was calculated.

A heatmap was then generated to visualize the correlations between numerical variables.

## 📈 Visualizations

The project includes the following visualizations:

* Sales by Category
* Sales Distribution Histogram
* Profit by Category
* Sales Distribution by Category
* Profit Distribution Box Plot
* Profit Variation Across Categories
* Discount vs Profit Scatter Plot
* Correlation Heatmap

## 🔍 Key Analysis Areas

The analysis focuses on:

**Sales Analysis**

* Category-wise sales performance
* Overall sales distribution

**Profit Analysis**

* Category-wise profit
* Profit variation and distribution

**Discount Analysis**

* Relationship between discount and profit

**Delivery Analysis**

* Number of days between order and shipping

**Correlation Analysis**

* Relationships among numerical variables

## 📁 Project Structure

```text
Task-2-BD/
│
├── Task_2_BD.ipynb
├── task_2_bd.py
└── README.md
```

## ▶️ How to Run

### Using Google Colab

1. Open `Task_2_BD.ipynb`.
2. Upload the Sample Superstore CSV dataset.
3. Update the dataset path if required.
4. Run all cells sequentially.

### Using Jupyter Notebook

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

Then open:

```text
Task_2_BD.ipynb
```

and execute the cells.

## ✅ Conclusion

This project demonstrates the use of **Python-based data analysis and visualization techniques** on the Sample Superstore dataset. The analysis helps understand sales, profit, discount, delivery time, category performance, and correlations between numerical variables.

The project provides a basic foundation for performing **Exploratory Data Analysis (EDA)** and extracting useful insights from business data.

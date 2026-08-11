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

##TASK -1
# Superstore Sales Data Analysis

## 📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on a Superstore Sales dataset using Python and Google Colab.

The analysis focuses on understanding the structure of the dataset, checking data quality, performing basic data preprocessing, calculating delivery time, analyzing sales by category, and creating visualizations.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Google Colab
* Google Drive

---

## 📂 Dataset

The dataset used in this project is:

**samplesuperstore.csv**

The dataset contains **10,194 records and 21 columns** before feature creation.

### Main Columns

* Row ID
* Order ID
* Order Date
* Ship Date
* Ship Mode
* Customer ID
* Customer Name
* Segment
* Country/Region
* City
* State/Province
* Postal Code
* Region
* Product ID
* Category
* Sub-Category
* Product Name
* Sales
* Quantity
* Discount
* Profit

---

## 🔎 Data Analysis Steps

### 1. Importing Libraries

The following Python libraries were imported:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

Pandas is used for data manipulation, NumPy for numerical operations, Matplotlib and Seaborn for data visualization.

---

### 2. Loading the Dataset

The Superstore CSV dataset was loaded using Pandas.

```python
df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/samplesuperstore.csv")
```

Google Drive was mounted to access the dataset from Google Colab.

---

### 3. Viewing the Dataset

The first five records were displayed using:

```python
df.head()
```

The dataset contains:

* 10,194 rows
* 21 columns

---

### 4. Dataset Information

The `df.info()` function was used to understand:

* Number of records
* Column names
* Data types
* Non-null values
* Memory usage

Initially, the dataset contained date columns as object/string data types.

---

### 5. Statistical Analysis

The `df.describe()` function was used to generate statistical summaries for numerical columns.

Important numerical columns include:

* Sales
* Quantity
* Discount
* Profit

The analysis showed that the average sales value is approximately **228.23**, while the average profit is approximately **28.67**.

---

### 6. Date Conversion

The `Order Date` and `Ship Date` columns were converted from object format to datetime format.

```python
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
```

This conversion allows date-based calculations and analysis.

---

### 7. Delivery Days Calculation

A new column named `Delivery Days` was created.

```python
df['Delivery Days'] = (
    df['Ship Date'] - df['Order Date']
).dt.days
```

This calculates the number of days taken to ship each order.

---

### 8. Category Analysis

The unique product categories were identified using:

```python
df['Category'].unique()
```

The dataset contains three main categories:

1. Furniture
2. Office Supplies
3. Technology

---

### 9. Missing Value Analysis

Missing values were checked using:

```python
df.isnull().sum()
```

The result showed that there were **no missing values** in any of the columns.

Therefore, no missing-value treatment was required at this stage.

---

## 📊 Sales Analysis by Category

Total sales were calculated using:

```python
category_sales = df.groupby('Category')['Sales'].sum()
```

### Results

| Category        |  Total Sales |
| --------------- | -----------: |
| Technology      | 839,893.2790 |
| Furniture       | 754,747.7613 |
| Office Supplies | 731,893.3140 |

### Key Observation

**Technology** generated the highest total sales among the three categories.

---

## 📈 Data Visualizations

### Sales by Category

A bar chart was created to compare total sales across different categories.

```python
category_sales.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.show()
```

The visualization clearly shows that Technology has the highest sales.

---

### Sales Distribution

A histogram was created using Seaborn to understand the distribution of sales values.

```python
plt.figure(figsize=(8,5))

sns.histplot(
    df['Sales'],
    bins=30
)

plt.title("Sales Distribution")
plt.show()
```

This visualization helps understand how frequently different sales values occur in the dataset.

---

## 🔑 Key Findings

* The dataset contains **10,194 records**.
* There are **21 original columns**.
* No missing values were found.
* The dataset contains three main categories:

  * Furniture
  * Office Supplies
  * Technology
* Technology generated the highest total sales.
* `Delivery Days` was successfully created from order and shipping dates.
* Sales distribution was visualized using a histogram.
* Category-wise sales were visualized using a bar chart.



---
Visualization:
outputs
1.
<img width="916" height="606" alt="image" src="https://github.com/user-attachments/assets/3ebae4fa-eacd-4552-a8dc-f25f11e26e40" />
2.
<img width="787" height="482" alt="image" src="https://github.com/user-attachments/assets/0eaea800-e45c-4101-a234-1e8128ce7766" />


## 🎯 Conclusion

This project demonstrates the basic steps involved in Exploratory Data Analysis using Python.

The dataset was successfully loaded, inspected, cleaned, transformed, and visualized. The analysis identified important sales patterns, including the strong performance of the Technology category.

Further analysis and visualization can be performed to obtain deeper business insights from the Superstore dataset.




# Task 2 – Big Data Analysis

# Superstore Sales Data Analysis – EDA

## 📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on a Superstore Sales dataset using Python.

The main objective is to understand sales, profit, discount, quantity, delivery time, and category-wise business performance through data analysis and visualization.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Google Colab

---

## 📂 Dataset

**Dataset:** `samplesuperstore.csv`

The dataset contains:

* **10,194 records**
* **21 original columns**

### Important Columns

* Order ID
* Order Date
* Ship Date
* Ship Mode
* Customer ID
* Customer Name
* Segment
* Region
* Category
* Sub-Category
* Product Name
* Sales
* Quantity
* Discount
* Profit

---

# 🔎 Exploratory Data Analysis

## 1. Importing Required Libraries

The required Python libraries were imported for data manipulation, numerical analysis, and visualization.

```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
```

### Purpose

* **Pandas** → Data manipulation and analysis
* **NumPy** → Numerical operations
* **Matplotlib** → Data visualization
* **Seaborn** → Statistical visualization

---

## 2. Loading the Dataset

The Superstore dataset was loaded using Pandas.

```python
df = pd.read_csv("/content/drive/MyDrive/samplesuperstore.csv")
```

The dataset was successfully loaded into a DataFrame named `df`.

---

## 3. Dataset Information

```python
df.info()
```

The `df.info()` function was used to inspect:

* Number of rows
* Number of columns
* Column names
* Data types
* Non-null values
* Memory usage

### Result

The dataset contains:

* **10,194 rows**
* **21 columns**
* No missing values
* 16 object columns
* 3 float columns
* 2 integer columns

Initially, `Order Date` and `Ship Date` were stored as object data types.

---

## 4. Statistical Summary

```python
df.describe()
```

The `describe()` function was used to obtain statistical information about numerical columns.

### Important observations

| Metric   |   Mean |
| -------- | -----: |
| Sales    | 228.23 |
| Quantity |   3.79 |
| Discount |  0.155 |
| Profit   |  28.67 |

The dataset also contains both positive and negative profit values.

The minimum profit is approximately **-6599.98**, while the maximum profit is approximately **8399.98**.

---

## 5. Date Conversion

The `Order Date` and `Ship Date` columns were converted into datetime format.

```python
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
```

### Purpose

Date conversion allows us to perform:

* Date calculations
* Monthly analysis
* Yearly analysis
* Delivery time analysis

---

## 6. Delivery Days Calculation

A new column called `Delivery Days` was created.

```python
df['Delivery Days'] = (
    df['Ship Date'] - df['Order Date']
).dt.days
```

### Purpose

This calculates the number of days between the order date and shipping date.

This feature can be used for future delivery performance analysis.

---

## 7. Category Identification

The unique product categories were identified.

```python
df['Category'].unique()
```

### Categories

* Office Supplies
* Furniture
* Technology

These categories are used for category-wise sales and profit analysis.

---

## 8. Missing Value Analysis

```python
df.isnull().sum()
```

Missing values were checked for every column.

### Result

All columns contained **0 missing values**.

Therefore, no missing-value treatment was required.

---

# 📊 Sales Analysis

## 9. Sales by Category

Total sales were calculated using `groupby()`.

```python
category_sales = df.groupby('Category')['Sales'].sum()
category_sales
```

### Result

| Category        |  Total Sales |
| --------------- | -----------: |
| Technology      | 839,893.2790 |
| Furniture       | 754,747.7613 |
| Office Supplies | 731,893.3140 |

### Observation

**Technology** generated the highest total sales.

Office Supplies generated the lowest total sales among the three categories.

---

## 10. Sales by Category – Bar Chart

```python
category_sales.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.show()
```

### Purpose

The bar chart provides a visual comparison of total sales between categories.

### Insight

Technology has the highest overall sales, followed by Furniture and Office Supplies.

---

## 11. Sales Distribution

A histogram was created to understand the distribution of sales values.

```python
plt.figure(figsize=(8,5))

sns.histplot(
    df['Sales'],
    bins=30
)

plt.title("Sales Distribution")
plt.show()
```

### Purpose

The histogram shows how frequently different sales values occur.

It helps identify the overall distribution and possible extreme sales values.

---

# 💰 Profit Analysis

## 12. Profit by Category

A bar plot was created to analyze profit across categories.

```python
sns.barplot(
    data=df,
    x="Category",
    y="Profit"
)

plt.title("Profit by Category")
plt.show()
```

### Purpose

To compare the average profit generated by each category.

### Insight

This visualization helps identify which category performs better in terms of average profitability.

---

## 13. Sales Distribution by Category

A category-wise sales bar plot was created.

```python
sns.barplot(
    data=df,
    x="Category",
    y="Sales"
)

plt.title("Sales Distribution by Category")
plt.show()
```

### Purpose

To compare the average sales value across different categories.

**Note:** This chart uses the average `Sales` per record, while the earlier `groupby().sum()` chart shows total sales.

---

## 14. Overall Profit Distribution

A boxplot was created to understand the distribution of profit.

```python
sns.boxplot(
    data=df,
    y="Profit"
)

plt.title("Profit Distribution")
plt.show()
```

### Purpose

The boxplot helps identify:

* Median profit
* Spread of profit
* Variability
* Outliers
* Negative profit values

The dataset contains several extreme profit values.

---

## 15. Profit Variation Across Categories

A category-wise boxplot was created.

```python
sns.boxplot(
    data=df,
    x="Category",
    y="Profit"
)

plt.title("Profit Variation Across Categories")
plt.show()
```

### Purpose

To compare profit distribution and variation among:

* Furniture
* Office Supplies
* Technology

This visualization also helps identify outliers within individual categories.

---

# 💸 Discount Analysis

## 16. Unique Discount Values

```python
df["Discount"].unique()
```

The dataset contains different discount percentages such as:

* 0
* 0.10
* 0.15
* 0.20
* 0.30
* 0.40
* 0.45
* 0.50
* 0.60
* 0.70
* 0.80

---

## 17. Discount vs Profit Analysis

A scatter plot was created to analyze the relationship between discount and profit.

```python
sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit"
)

plt.title("Impact of Discount on Profit")
plt.show()
```

### Purpose

To investigate whether increasing discounts are associated with changes in profit.

### Correlation Result

The correlation between Discount and Profit is approximately:

**-0.219**

This indicates a **weak negative relationship** between discount and profit.

In general, higher discounts are associated with lower profit, although correlation does not prove causation.

---

# 🔗 Correlation Analysis

## 18. Selecting Numerical Columns

```python
numeric_df = df.select_dtypes(
    include="number"
)
```

Only numerical columns were selected for correlation analysis.

The numerical columns include:

* Row ID
* Sales
* Quantity
* Discount
* Profit
* Delivery Days

---

## 19. Correlation Matrix

```python
corr = numeric_df.corr()

corr
```

The correlation matrix was calculated to understand relationships between numerical variables.

### Important Correlations

| Variables              | Correlation |
| ---------------------- | ----------: |
| Sales – Profit         |       0.481 |
| Discount – Profit      |      -0.219 |
| Sales – Quantity       |       0.198 |
| Quantity – Profit      |       0.066 |
| Delivery Days – Profit |      -0.004 |

### Key Observations

* **Sales and Profit** have a moderate positive relationship.
* **Discount and Profit** have a weak negative relationship.
* **Sales and Quantity** have a weak positive relationship.
* **Delivery Days and Profit** have almost no linear relationship.

---

## 20. Correlation Heatmap

A heatmap was created to visually represent the correlation matrix.

```python
sns.heatmap(
    corr,
    annot=True
)

plt.title("Correlation Heatmap")
plt.show()
```

### Purpose

The heatmap makes it easier to identify positive and negative relationships between numerical variables.

Higher positive values indicate stronger positive relationships, while negative values indicate inverse relationships.

---

# 📌 Key Findings

Based on the EDA:

1. The dataset contains **10,194 records**.
2. There are **21 original columns**.
3. No missing values were detected.
4. The dataset contains three major categories:

   * Furniture
   * Office Supplies
   * Technology
5. Technology generated the highest total sales.
6. Delivery Days was successfully calculated using Order Date and Ship Date.
7. Sales and Profit have a moderate positive correlation of approximately **0.481**.
8. Discount and Profit have a weak negative correlation of approximately **-0.219**.
9. The dataset contains negative profit values and significant profit outliers.
10. Category-wise boxplots show variation in profitability.
11. Sales distribution contains relatively high-value observations.
12. Delivery Days has almost no linear correlation with Profit.

---

# 📈 Visualizations Created

The following visualizations were created during the analysis:

1. Sales by Category – Bar Chart
2. Sales Distribution – Histogram
3. Profit by Category – Bar Plot
4. Sales Distribution by Category – Bar Plot
5. Profit Distribution – Box Plot
6. Profit Variation Across Categories – Box Plot
7. Discount vs Profit – Scatter Plot
8. Correlation Heatmap

---

outputs:
1. Sales by Category – Bar Chart
<img width="842" height="602" alt="image" src="https://github.com/user-attachments/assets/a9216b12-7a41-4840-a1d5-27818f51b14e" />
2. Sales Distribution – Histograz
<img width="780" height="527" alt="image" src="https://github.com/user-attachments/assets/88d8bccc-6e84-4207-a2a8-0890be076e1b" />
3. Profit by Category – Bar Plot
<img width="671" height="497" alt="image" src="https://github.com/user-attachments/assets/f6610a7b-c13e-463a-8000-4fef3673d134" />
5. Sales Distribution by Category – Bar Plot
<img width="688" height="486" alt="image" src="https://github.com/user-attachments/assets/a38f323d-5b55-4b4c-a40d-2421393a6fe3" />
6.Profit Distribution – Box Plot
<img width="695" height="437" alt="image" src="https://github.com/user-attachments/assets/1e9dfc81-e3f6-4bcf-b3da-f74236a10f32" />
7. Profit Variation Across Categories – Box Plot
8. <img width="755" height="467" alt="image" src="https://github.com/user-attachments/assets/2865b1de-0fab-49df-8d1b-f8062b04f580" />
9. Discount vs Profit – Scatter Plot
<img width="672" height="480" alt="image" src="https://github.com/user-attachments/assets/855464f4-7863-4f08-aa83-81523f49a630" />
10. Correlation Heatmap
<img width="718" height="557" alt="image" src="https://github.com/user-attachments/assets/0aa2a21b-9038-4ad1-924c-f688feb72855" />


# 🎯 Conclusion

This project demonstrates an end-to-end Exploratory Data Analysis workflow using Python.

The dataset was successfully loaded, inspected, transformed, analyzed, and visualized.

The analysis provides useful insights into sales performance, profitability, discount behavior, category performance, and relationships between numerical variables.

The results can be used as a foundation for advanced business analytics, predictive modeling, and dashboard development.

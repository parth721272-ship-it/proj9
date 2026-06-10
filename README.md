# 📊 Sales Data Analyzer

## 📌 Project Overview

Sales Data Analyzer is a Python-based data analysis project that uses Pandas, NumPy, Matplotlib, and Seaborn to analyze sales data stored in a CSV file.

The project provides various data analysis features such as:

- Data Exploration
- Data Cleaning
- Mathematical Operations
- Search, Sort, and Filter
- Aggregation Functions
- Statistical Analysis
- Pivot Tables
- Data Visualization

This project is suitable for beginners learning Python Data Analysis.

---

# 🎯 Objectives

- Learn data analysis using Pandas
- Understand data cleaning techniques
- Perform statistical calculations
- Create visualizations using Matplotlib and Seaborn
- Work with CSV datasets
- Apply Object-Oriented Programming (OOP) concepts

---

# 🛠 Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# 📂 Project Structure

Sales_Data_Analyzer/

├── sales_data_analyzer.py

├── sales_data.csv

├── bar_chart.png

├── line_chart.png

├── scatter_chart.png

└── README.md

---

# 📊 Dataset Format

Create a file named `sales_data.csv`

```csv
Date,Region,Product,Sales,Profit
2025-01-01,North,Laptop,50000,12000
2025-01-02,South,Mobile,30000,7000
2025-01-03,East,Tablet,25000,5000
2025-01-04,West,Laptop,45000,10000
2025-01-05,North,Mobile,35000,8000
2025-01-06,South,Tablet,20000,4000
2025-01-07,East,Laptop,55000,13000
2025-01-08,West,Mobile,28000,6000
```

---

# ⚙ Features

## 1. Data Exploration

Displays:

- First 5 rows
- Dataset information
- Statistical summary

Methods Used:

```python
head()
info()
describe()
```

---

## 2. Data Cleaning

Removes:

- Duplicate records
- Missing values

Methods Used:

```python
drop_duplicates()
fillna()
```

---

## 3. Mathematical Operations

Calculates:

- Total Sales
- Average Sales
- Maximum Sales
- Minimum Sales

Methods Used:

```python
sum()
mean()
max()
min()
```

---

## 4. Search, Sort and Filter

Features:

- Filter sales greater than 30000
- Sort data by sales

Methods Used:

```python
sort_values()
```

---

## 5. Aggregate Functions

Groups data by Region and calculates:

- Sum
- Mean
- Count

Methods Used:

```python
groupby()
agg()
```

---

## 6. Statistical Analysis

Calculates:

- Standard Deviation
- Variance
- Quantiles

Methods Used:

```python
std()
var()
quantile()
```

---

## 7. Pivot Table

Creates a pivot table using:

```python
pd.pivot_table()
```

Example Output:

| Region | Laptop | Mobile | Tablet |
|----------|----------|----------|----------|
| East | 55000 | 0 | 25000 |
| North | 50000 | 35000 | 0 |
| South | 0 | 30000 | 20000 |
| West | 45000 | 28000 | 0 |

---

## 8. Data Visualization

### Bar Chart

Sales by Product

Output File:

```text
bar_chart.png
```

### Line Chart

Sales Trend by Date

Output File:

```text
line_chart.png
```

### Scatter Plot

Sales vs Profit

Output File:

```text
scatter_chart.png
```

---

# ▶ How to Run the Project

## Step 1: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

## Step 2: Place Dataset

Save the dataset as:

```text
sales_data.csv
```

in the same folder as the Python file.

## Step 3: Run the Program

```bash
python sales_data_analyzer.py
```

---

# 📋 Menu Options

```text
===== SALES DATA ANALYZER =====

1. Explore Data
2. Clean Data
3. Mathematical Operations
4. Search/Sort/Filter
5. Aggregate Functions
6. Statistical Analysis
7. Pivot Table
8. Visualizations
9. Exit
```

---

# 📚 Python Concepts Used

## Object-Oriented Programming (OOP)

- Class
- Object
- Constructor (__init__)
- Destructor (__del__)
- Methods

## Pandas Functions

```python
read_csv()
head()
info()
describe()
groupby()
pivot_table()
concat()
sort_values()
```

## NumPy

Used for numerical and mathematical operations.

## Matplotlib

Used for:

- Bar Charts
- Line Charts

## Seaborn

Used for:

- Scatter Plot

---

# Gujarati Explanation (English Letters)

Aa project sales data analyze karva mate banavyo che.

User CSV file mathi sales data load kari shake che.

Project ni madad thi:

- Data explore kari shakay che
- Missing values remove kari shakay che
- Total, Average, Maximum ane Minimum sales calculate kari shakay che
- Sales data sort ane filter kari shakay che
- Region wise aggregation kari shakay che
- Statistical analysis kari shakay che
- Pivot table banavi shakay che
- Bar chart, line chart ane scatter plot generate kari shakay che

Aa project beginner mate Pandas, NumPy, Matplotlib ane Seaborn sikhva mate khub upyogi che.

---

# Author

**Sales Data Analyzer**

Python Data Analysis Project for Beginners 🚀

# Lab 3: Data Preprocessing, EDA, NumPy, Pandas, Visualization

## Problem Statement
Explore and prepare raw data for machine learning models using Python's core data science libraries. The task involves handling missing values, performing Exploratory Data Analysis (EDA), and generating statistical visualizations.

## Tools & Libraries Used
1. **NumPy:** Used for high-performance numerical computations and handling arrays.
2. **Pandas:** Used for data manipulation, creating DataFrames, handling missing values (imputation), and basic statistical summaries.
3. **Matplotlib & Seaborn:** Used for generating graphical representations of data (histograms, scatter plots) to uncover patterns and anomalies.

## Approach: Exploratory Data Analysis (EDA)
EDA is the process of investigating datasets to discover patterns, spot anomalies, and test hypotheses. 
1. **Data Ingestion:** Load data into a Pandas DataFrame.
2. **Preprocessing:** Identify `NaN` (Not a Number) values. We replace missing numerical values with the mean/median and categorical values with the mode.
3. **Outlier Treatment:** Identify anomalous data points (e.g., Age = 120) and cap them.
4. **Visualization:** Plot the cleaned data to understand distributions and correlations between variables like Age and Salary.

## Expected Output
Running the script will output the initial raw DataFrame, the cleaned DataFrame after imputation, and a statistical summary to the console. It will then open a GUI window displaying a side-by-side Histogram and Scatter Plot.
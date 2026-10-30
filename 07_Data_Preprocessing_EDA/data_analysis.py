import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    print("--- 1. NumPy Basics ---")
    # Create a 1D array and perform basic mathematical operations
    np_data = np.array([12, 15, 14, 19, 22, np.nan, 25, 29])
    print(f"Original NumPy Array: {np_data}")
    print(f"Mean (ignoring NaN): {np.nanmean(np_data):.2f}\n")

    print("--- 2. Pandas & Data Preprocessing ---")
    # Create a dummy dataset with missing values and outliers
    raw_data = {
        'Age': [25, 27, 29, np.nan, 32, 35, 40, 120],  # 120 is an outlier
        'Salary': [50000, 54000, 58000, 60000, np.nan, 65000, 70000, 72000],
        'Department': ['IT', 'HR', 'IT', 'Marketing', 'IT', 'HR', np.nan, 'Marketing']
    }
    df = pd.DataFrame(raw_data)
    
    print("Initial DataFrame:")
    print(df, "\n")

    # Handling missing values (Imputation)
    print("Handling Missing Values...")
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
    df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
    
    # Handling outliers (Cap age at 60)
    df.loc[df['Age'] > 60, 'Age'] = 60

    print("\nPreprocessed DataFrame:")
    print(df, "\n")

    print("--- 3. Exploratory Data Analysis (EDA) ---")
    print("Summary Statistics:")
    print(df.describe(), "\n")
    
    print("Department Counts:")
    print(df['Department'].value_counts())

    print("\n--- 4. Data Visualization ---")
    print("Generating plots... (Close the plot windows to terminate the script)")
    
    # Set up the matplotlib figure
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Histogram of Ages (Visualization)
    sns.histplot(df['Age'], bins=5, kde=True, ax=axes[0], color='blue')
    axes[0].set_title('Age Distribution')
    
    # Plot 2: Scatter plot of Age vs Salary
    sns.scatterplot(data=df, x='Age', y='Salary', hue='Department', ax=axes[1], s=100)
    axes[1].set_title('Age vs Salary by Department')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
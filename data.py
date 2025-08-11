# --- 1. Import Libraries ---
import pandas as pd
import matplotlib.pyplot as plt

# --- 2. Load CSV ---
# Replace 'sales.csv' with your actual dataset file
df = pd.read_csv("sales.csv")

# --- 3. Basic Data Exploration ---
print("First 5 rows:")
print(df.head())

print("\nShape of DataFrame (rows, columns):", df.shape)
print("\nColumn Names:", df.columns.tolist())

print("\nData Info:")
print(df.info())

print("\nMissing Values per Column:")
print(df.isnull().sum())

# --- 4. Basic Statistics ---
print("\nSummary Statistics:")
print(df.describe())

# --- 5. Groupby Example ---
# Example: Group by 'Product' and sum 'Sales'
if 'Product' in df.columns and 'Sales' in df.columns:
    product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
    print("\nTotal Sales by Product:\n", product_sales)

    # --- 6. Visualization ---
    plt.figure(figsize=(8,5))
    product_sales.plot(kind="bar", color="skyblue")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# --- 7. Filtering Example ---
# Example: Filter rows where Sales > 500
if 'Sales' in df.columns:
    high_sales = df[df["Sales"] > 500]
    print("\nRows with Sales > 500:\n", high_sales)

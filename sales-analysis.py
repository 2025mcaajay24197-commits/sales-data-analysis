import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())

# Total Sales
print("\nTotal Sales:", df["Sales"].sum())

# Category-wise Sales
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

# Sub-category (Top 5)
print("\nTop Sub-Categories:")
print(df.groupby("Sub Category")["Sales"].sum().sort_values(ascending=False).head(5))

df["Order Date"] = pd.to_datetime(df["Order Date"], format='mixed', dayfirst=True)

df["Month"] = df["Order Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)
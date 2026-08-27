import pandas as pd

df = pd.read_csv(r"C:\Users\shari\Downloads\sales_data.csv")

print("=" * 60)
print("           SALES DATA ANALYSIS")
print("=" * 60)

print("\n FIRST 5 ROWS")
print("-" * 60)
print(df.head())

print("\n DATASET SHAPE")
print("-" * 60)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n COLUMN NAMES")
print("-" * 60)
print(df.columns.tolist())

print("\n DATA TYPES")
print("-" * 60)
print(df.dtypes)

print("\n MISSING VALUES BEFORE CLEANING")
print("-" * 60)
print(df.isnull().sum())

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

df["Total_Sales"] = pd.to_numeric(df["Total_Sales"], errors="coerce")

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

df["Total_Sales"] = df["Total_Sales"].fillna(df["Total_Sales"].median())

duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

print("\n DATA CLEANING")
print("-" * 60)
print(f"Duplicate rows removed: {duplicates_removed}")

print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())

total_revenue = df["Total_Sales"].sum()

average_sales = df["Total_Sales"].mean()

highest_sale = df["Total_Sales"].max()

lowest_sale = df["Total_Sales"].min()

total_quantity = df["Quantity"].sum()

product_sales = df.groupby("Product")["Total_Sales"].sum()

best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

product_report = (
    df.groupby("Product")
    .agg(
        Total_Quantity=("Quantity", "sum"),
        Total_Revenue=("Total_Sales", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
)


print("\n" + "=" * 60)
print("              SALES REPORT")
print("=" * 60)

print(f"\n Total Revenue      : ₹{total_revenue:,.2f}")
print(f" Total Quantity     : {total_quantity:,.0f}")
print(f" Average Sale      : ₹{average_sales:,.2f}")
print(f"⬆ Highest Sale      : ₹{highest_sale:,.2f}")
print(f"⬇ Lowest Sale       : ₹{lowest_sale:,.2f}")

print(f"\n Best-Selling Product: {best_product}")
print(f" Product Revenue     : ₹{best_product_sales:,.2f}")


print("\n PRODUCT-WISE PERFORMANCE")
print("-" * 60)
print(product_report)


print("\n" + "=" * 60)
print("              ANALYSIS COMPLETE")
print("=" * 60)
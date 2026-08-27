# 📊 Sales Data Analysis

A lightweight, no-frills Python script that cleans a raw sales CSV, crunches the key numbers, and prints a formatted report straight to your terminal — no dashboards, no dependencies beyond pandas.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## ✨ Overview

This script takes a messy `sales_data.csv` file and turns it into a clean, readable sales report. It handles missing values, removes duplicates, and generates both summary statistics and a product-wise performance breakdown — all printed in a clean, structured console output.

---

## 🚀 Features

- 🔍 **Data Inspection** — Instantly view shape, column names, and data types
- 🧹 **Automated Cleaning** — Coerces bad values to numeric, fills missing entries with the median, and drops duplicate rows
- 📈 **Key Metrics** — Total revenue, total quantity sold, average/highest/lowest sale
- 🏆 **Best-Seller Detection** — Identifies the top-performing product by revenue
- 📦 **Product-Wise Report** — Aggregated quantity and revenue per product, sorted by performance
- 🖥️ **Clean Console Output** — Neatly formatted, section-by-section terminal report

---

## 🗂️ Project Structure

sales-data-analysis/
│
├── sales_analysis.py # Main analysis script
├── sales_data.csv # Input dataset (not included — add your own)
└── README.md # You're here


---

## ⚙️ Requirements

- Python 3.8+
- pandas

Install the dependency:

```bash
pip install pandas
```

---

## ▶️ Usage

1. Place your `sales_data.csv` file in the project directory (or update the file path in the script).
2. Ensure your CSV includes at least the following columns:
   - `Product`
   - `Quantity`
   - `Total_Sales`
3. Run the script:

```bash
python sales_analysis.py
```

> 💡 **Tip:** Update the hardcoded path (`C:\Users\shari\Downloads\sales_data.csv`) to a relative path like `"sales_data.csv"` before sharing or running on another machine.

---

## 📋 Sample Output
============================================================
SALES REPORT

Total Revenue : ₹1,245,890.00
Total Quantity : 8,432
Average Sale : ₹1,482.65
⬆ Highest Sale : ₹58,000.00
⬇ Lowest Sale : ₹120.00

Best-Selling Product: Wireless Headphones
Product Revenue : ₹312,450.00

PRODUCT-WISE PERFORMANCE
                 Total_Quantity  Total_Revenue

Product
Wireless Headphones 1200 312450
Smart Watch 980 289100
...


---

## 🧠 How It Works

| Step | Description |
|------|-------------|
| 1️⃣ Load | Reads the CSV into a pandas DataFrame |
| 2️⃣ Inspect | Prints shape, columns, dtypes, and missing values |
| 3️⃣ Clean | Converts `Quantity`/`Total_Sales` to numeric, fills nulls with median, drops duplicates |
| 4️⃣ Analyze | Computes revenue, quantity, and sale-level statistics |
| 5️⃣ Aggregate | Groups by `Product` for a revenue-ranked performance table |
| 6️⃣ Report | Prints a formatted summary and detailed breakdown |

---

## 🛣️ Possible Improvements

- [ ] Export cleaned data and reports to CSV/Excel
- [ ] Add data visualizations (matplotlib/seaborn charts)
- [ ] Accept file path as a command-line argument
- [ ] Add unit tests for the cleaning logic
- [ ] Wrap analysis in functions/classes for reusability

---

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and share.

---

## 🙌 Author

Built with pandas and a love for clean data. Contributions and suggestions welcome!

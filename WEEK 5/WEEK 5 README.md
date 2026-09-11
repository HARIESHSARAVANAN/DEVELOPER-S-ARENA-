
<div align="center">

# 📊 CUSTOMER SALES ANALYSIS

### 🚀 ADVANCED DATA MANIPULATION WITH PANDAS

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=2F81F7&center=true&vCenter=true&width=700&lines=Analyzing+Customer+Sales+Data;Exploring+Products+%26+Regions;Finding+Business+Insights;Powered+by+Python+%26+Pandas" />

<br>

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/NumPy-Numerical%20Analysis-013243?style=for-the-badge&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge">
<img src="https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white">

<br><br>

<img src="https://img.shields.io/badge/Transactions-100-success?style=flat-square">
<img src="https://img.shields.io/badge/Customers-100-blue?style=flat-square">
<img src="https://img.shields.io/badge/Products-5-purple?style=flat-square">
<img src="https://img.shields.io/badge/Regions-4-orange?style=flat-square">

</div>

---

# 🎯 PROJECT OVERVIEW

**Customer Sales Analysis** is a data analysis project developed as part of **Week 5: Advanced Data Manipulation with Pandas**.

The project transforms raw sales transaction data into meaningful business insights using Python and Pandas.

The analysis focuses on:

- 👥 Customer behavior
- 📦 Product performance
- 🌍 Regional sales
- 📅 Monthly sales trends
- 💰 Revenue analysis
- 🎯 Customer segmentation
- 📊 Business KPIs
- 🔗 Data merging and enrichment

---

# 🧰 TECHNOLOGY STACK

| TECHNOLOGY | PURPOSE |
|---|---|
| 🐍 Python | Programming Language |
| 🐼 Pandas | Data Manipulation & Analysis |
| 🔢 NumPy | Numerical Operations |
| 📊 Matplotlib | Data Visualization |
| 📓 Jupyter Notebook | Interactive Analysis |
| 🐙 Git & GitHub | Version Control |

---

# 📂 PROJECT STRUCTURE

```text
WEEK 5/
│
├── 📁 DAY 1/
│   └── Data Exploration Screenshots
│
├── 📁 DAY 2/
│   └── Data Cleaning Screenshots
│
├── 📁 DAY 3/
│   └── Customer Analysis Screenshots
│
├── 📁 DAY 4/
│   └── Sales Pattern Screenshots
│
├── 📁 DAY 5/
│   └── Advanced Analysis Screenshots
│
├── 📁 DAY 6/
│   └── Dashboard & KPI Screenshots
│
├── 📓 customer_analysis.ipynb
├── 📊 sales_data.csv
├── 👥 customer_churn.csv
├── ⚙️ requirements.txt
├── 📄 WEEK 5 report.md
└── 📖 README.md
🔎 ANALYSIS WORKFLOW
<div align="center">
       📥 RAW DATA
           │
           ▼
    🧹 DATA CLEANING
           │
           ▼
    🔍 DATA EXPLORATION
           │
           ▼
    👥 CUSTOMER ANALYSIS
           │
           ▼
    📦 PRODUCT ANALYSIS
           │
           ▼
    🌍 REGIONAL ANALYSIS
           │
           ▼
     📅 SALES TRENDS
           │
           ▼
    📊 ADVANCED ANALYSIS
           │
           ▼
      📈 DASHBOARD
           │
           ▼
    💡 BUSINESS INSIGHTS
</div>
📊 KEY PERFORMANCE INDICATORS
<div align="center">
💰 TOTAL REVENUE	🧾 AVG TRANSACTION	👥 CUSTOMERS
₹12,365,048	₹123,650.48	100
🏆 BEST PRODUCT	🌍 BEST REGION	📅 BEST MONTH
Laptop	North	March
</div>
🏆 TOP PRODUCT PERFORMANCE
PRODUCT	TOTAL SALES
💻 Laptop	₹3,889,210
📱 Tablet	₹2,884,340
📱 Phone	₹2,859,394
🎧 Headphones	₹1,384,033
🖥️ Monitor	₹1,348,071
🥇 BEST PRODUCT

Laptop generated the highest total revenue:

💰 ₹3,889,210

It also recorded the highest number of units sold:

📦 136 units

🌍 REGIONAL PERFORMANCE
REGION	TOTAL SALES
🥇 North	₹3,983,635
🥈 South	₹3,737,852
🥉 East	₹2,519,639
West	₹2,123,922
🌟 TOP REGION

North was the highest-performing region with:

💰 ₹3,983,635

📅 MONTHLY SALES
MONTH	TOTAL SALES
January	₹4,120,524
February	₹2,656,050
🥇 March	₹4,485,006
April	₹1,103,468
📈 HIGHEST SALES MONTH

March

💰 ₹4,485,006

📉 LOWEST SALES MONTH

April

💰 ₹1,103,468

🐼 PANDAS TECHNIQUES USED

The project demonstrates several important Pandas techniques:

groupby()
agg()
sum()
mean()
count()
nunique()
sort_values()
pivot_table()
merge()
pd.cut()
🔥 DATA MANIPULATION
Grouping and aggregation
Multi-condition filtering
Pivot tables
Data merging
Customer segmentation
Sorting and ranking
Date-time manipulation
Data validation
String cleaning
🧹 DATA QUALITY

The dataset was validated before analysis.

CHECK	RESULT
Missing Values	✅ 0
Duplicate Records	✅ 0
Sales Calculation Errors	✅ 0
Valid Transactions	✅ 100

The Total_Sales column was validated using:

Quantity × Price = Total_Sales

All 100 transactions passed validation.

🔗 DATA MERGING

The project demonstrates a valid Pandas merge operation.

The sales dataset and customer churn dataset were inspected for integration.

However, the datasets use different customer ID formats:

Sales Dataset
CUST001
CUST002
CUST003

Customer Churn Dataset
C00001
C00002
C00003

Since there was no valid mapping between these identifiers, they were not artificially joined.

Instead, a product-level summary was created and merged with the sales dataset using the common Product field.

MERGE VALIDATION
Original Records : 100
Merged Records   : 100
Unmatched        : 0
👥 CUSTOMER ANALYSIS

Customer-level analysis identified:

👤 100 unique customers
🏆 Highest-value customer: CUST016
💰 Highest customer spending: ₹373,932
🧾 Average transaction: ₹123,650.48
🔁 Repeat customers: 0

Since each customer appears only once in the available transaction history, deeper retention and lifetime-value analysis is limited.

🎯 CUSTOMER SEGMENTATION

Transactions were divided into three value-based segments:

SEGMENT	TRANSACTION VALUE
🟢 Low Value	₹0 – ₹100,000
🟡 Medium Value	₹100,000 – ₹200,000
🔴 High Value	Above ₹200,000

This segmentation can help businesses develop targeted strategies for different transaction-value groups.

💡 BUSINESS INSIGHTS
🏆 PRODUCT PERFORMANCE

Laptop is the strongest-performing product by revenue and units sold.

🌍 REGIONAL PERFORMANCE

North generates the highest regional revenue.

📅 MONTHLY PERFORMANCE

March recorded the highest monthly sales, while April recorded the lowest.

👥 CUSTOMER BEHAVIOR

The dataset contains one transaction per customer, limiting repeat-purchase analysis.

📊 ANALYTICAL OPPORTUNITY

Longer-term transaction data would enable deeper customer retention and lifetime-value analysis.

🚀 BUSINESS RECOMMENDATIONS
💻 1. STRENGTHEN LAPTOP SALES

Focus on the highest-performing product and investigate the factors driving its success.

🌍 2. STUDY NORTH REGION

Analyze pricing, customer preferences, promotions, and product availability in North.

📉 3. IMPROVE WEST PERFORMANCE

Develop targeted strategies to improve sales in the lowest-performing region.

📅 4. INVESTIGATE MARCH SALES

Identify whether promotions, seasonality, or other factors contributed to March's strong performance.

👥 5. COLLECT LONGER CUSTOMER HISTORIES

More transaction data would enable meaningful retention and customer lifetime-value analysis.

📸 PROJECT DOCUMENTATION

The repository contains screenshots documenting the development process across:

DAY 1 → DATA EXPLORATION
DAY 2 → DATA CLEANING
DAY 3 → CUSTOMER ANALYSIS
DAY 4 → SALES PATTERNS
DAY 5 → ADVANCED ANALYSIS
DAY 6 → DASHBOARD & KPIs

These screenshots provide visual evidence of the analysis workflow.

📓 NOTEBOOK

The complete analysis is available in:

customer_analysis.ipynb

The notebook contains the complete Python implementation, analysis, visualizations, KPIs, and business insights.

📄 PROJECT REPORT

The detailed project report is available in:

WEEK 5 report.md

The report contains the complete analysis methodology, findings, recommendations, and conclusion.

⚙️ INSTALLATION

Clone the repository:

git clone https://github.com/HARIESHSARAVANAN/DEVELOPER-S-ARENA-.git

Navigate to Week 5:

cd "DEVELOPER-S-ARENA-/WEEK 5"

Install the required libraries:

pip install -r requirements.txt

Launch Jupyter Notebook:

jupyter notebook

Open:

customer_analysis.ipynb
▶️ HOW TO RUN
Clone the repository.
Navigate to the WEEK 5 directory.
Install the dependencies.
Open customer_analysis.ipynb.
Run the notebook cells from top to bottom.
Explore the generated visualizations and insights.
🧪 VALIDATION

The notebook was tested by running all cells from a fresh kernel.

TEST RESULT
╔══════════════════════════════════════╗
║          NOTEBOOK VALIDATION         ║
╠══════════════════════════════════════╣
║ Cells Executed       : ✅ SUCCESS    ║
║ Errors               : ✅ NONE       ║
║ Missing Values       : ✅ 0          ║
║ Duplicate Records    : ✅ 0          ║
║ Sales Validation     : ✅ 100/100    ║
╚══════════════════════════════════════╝
🌟 FINAL OUTCOME

The project successfully demonstrates how Pandas can transform raw transaction data into actionable business intelligence.

From data cleaning to advanced manipulation, visualization, KPI generation, and business recommendations, the project provides an end-to-end data analysis workflow.

<div align="center">
📊 DATA → 🔍 ANALYSIS → 💡 INSIGHTS → 🚀 DECISIONS
<br>

BUILT WITH 🐍 PYTHON + 🐼 PANDAS + 📊 MATPLOTLIB

<br>

⭐ THANK YOU FOR VISITING THIS PROJECT! ⭐

</div>

<div align="center">

# 📊 WEEK 8 | CUSTOMER CHURN & RETENTION STRATEGY

### End-to-End Real-World Business Analysis Capstone

<img src="https://img.shields.io/badge/Python-Data%20Science-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-Analytics-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--Learn-Predictive%20Modeling-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,50:764ba2,100:f093fb&height=170&section=header&text=CUSTOMER%20CHURN%20%26%20RETENTION&fontSize=31&fontColor=ffffff&animation=fadeIn&fontAlignY=35" width="100%"/>

</div>

---

## 🧠 EXECUTIVE OVERVIEW

This capstone answers a practical business question:

> **Which customer characteristics are associated with churn, and how can a business prioritize retention efforts using data?**

**Business Problem → Data Cleaning → EDA → Statistical Analysis → Predictive Modeling → Recommendations → Implementation**

---

## 📊 KPI DASHBOARD

<div align="center">

| 👥 Customers | 🔥 Churn Rate | ⏱️ Avg Tenure | 💳 Avg Monthly Charges | 🤖 ROC-AUC |
|:---:|:---:|:---:|:---:|:---:|
| **500** | **10.6%** | **36.53 mo** | **$113.64** | **0.987** |

</div>

---

# 🎯 BUSINESS PROBLEM

A subscription business is losing customers. This project investigates:

- Which customer groups show higher churn?
- Is tenure associated with churn?
- Are monthly charges different between churn groups?
- Does contract type show different churn behavior?
- Can a baseline model prioritize customers for retention review?
- What actions can the business test?

---

# 🗂️ PROJECT ARCHITECTURE

```text
RAW DATA
   ↓
DATA CLEANING
   ↓
EDA & VISUAL STORY
   ↓
STATISTICAL TESTING
   ↓
LOGISTIC REGRESSION
   ↓
BUSINESS INSIGHTS
   ↓
RETENTION ACTIONS
   ↓
MEASUREMENT & ITERATION
```

---

# 📁 PROJECT STRUCTURE

```text
WEEK 8/
├── README.md
├── capstone_analysis.ipynb
├── requirements.txt
│
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── notebooks/
│   ├── 1_data_cleaning.ipynb
│   ├── 2_eda.ipynb
│   └── 3_analysis.ipynb
│
├── reports/
│   ├── executive_summary.pdf
│   └── technical_report.pdf
│
├── presentation/
│   └── business_presentation.pptx
│
└── portfolio/
    └── portfolio_page.html
```

---

# 🔬 ANALYSIS TECHNIQUES

### 📊 Exploratory Data Analysis
Distribution analysis, group comparisons, contract analysis, payment analysis and tenure segmentation.

### 🧪 Statistical Testing

| Test | p-value |
|---|---:|
| Tenure vs Churn | **8.98e-130** |
| Monthly Charges vs Churn | **0.0101** |
| Contract vs Churn | **9.59e-07** |
| Payment Method vs Churn | **0.144** |
| Paperless Billing vs Churn | **0.829** |

### 🤖 Predictive Modeling

A baseline Logistic Regression model uses tenure, charges, senior-citizen status, contract, payment method and paperless billing.

| Metric | Result |
|---|---:|
| Accuracy | **0.944** |
| Precision | **0.650** |
| Recall | **1.000** |
| F1 | **0.788** |
| ROC-AUC | **0.987** |

---

# 📈 VISUAL STORY

### Customer Churn
![Churn](visualizations/01_churn_distribution.png)

### Tenure
![Tenure](visualizations/02_tenure_by_churn.png)

### Monthly Charges
![Charges](visualizations/03_monthly_charges_by_churn.png)

### Contract
![Contract](visualizations/04_churn_by_contract.png)

### Payment Method
![Payment](visualizations/05_churn_by_payment_method.png)

### Correlation
![Correlation](visualizations/06_correlation_heatmap.png)

### Tenure Segmentation
![Tenure Bands](visualizations/07_churn_by_tenure_band.png)

### Model Performance
![ROC](visualizations/08_roc_curve.png)

![Confusion Matrix](visualizations/09_confusion_matrix.png)

---

# 💡 KEY BUSINESS FINDINGS

## 🔥 1. Early-tenure customers are a major retention segment

Retained customers average **40.2 months** of tenure, while churned customers average **6.0 months**.

The difference is statistically significant:

**p = 8.98e-130**

This supports testing stronger onboarding and early-life engagement.

## 📑 2. Contract type shows a strong business signal

Observed churn:

- Month-to-month: **20.6%**
- One year: **4.3%**
- Two year: **6.9%**

Contract vs Churn:

**p = 9.59e-07**

This is an association, not proof that changing contract type causes lower churn.

## 💳 3. Monthly charges differ between churn groups

Retained average: **$111.72**

Churned average: **$129.77**

Welch t-test:

**p = 0.0101**

## 🤖 4. A baseline model can prioritize human review

The Logistic Regression model achieved:

**ROC-AUC = 0.987**

It should be used for prioritization and validated on future data.

---

# 🚀 IMPLEMENTATION PLAN

### PHASE 1 · DATA & MODEL VALIDATION
Validate the pipeline and test performance on newer data.

### PHASE 2 · RISK REPORTING
Create a weekly list of customers with elevated predicted churn risk.

### PHASE 3 · EARLY-TENURE INTERVENTION
Strengthen onboarding and engagement during the first year.

### PHASE 4 · CONTRACT EXPERIMENTATION
Test renewal reminders, loyalty benefits and contract education.

### PHASE 5 · MEASURE & ITERATE
Track churn reduction, retention uplift, intervention cost and customer response.

---

# ⚠️ LIMITATIONS

The supplied dataset contains **500 customers**, but it does not contain:

```text
❌ Revenue
❌ Profit
❌ Acquisition Cost
❌ Campaign Spend
❌ Customer Lifetime Value
❌ Intervention History
```

Therefore, this project does not invent ROI figures.

The model is a **baseline analytical tool**, not a production-ready automated decision system.

---

# 🛠️ SETUP

```bash
pip install -r requirements.txt
jupyter notebook capstone_analysis.ipynb
```

Or run the stages individually:

```bash
jupyter notebook notebooks/1_data_cleaning.ipynb
jupyter notebook notebooks/2_eda.ipynb
jupyter notebook notebooks/3_analysis.ipynb
```

---

# 📦 WEEK 8 REQUIREMENTS

| Requirement | Status |
|---|:---:|
| 500+ rows | ✅ |
| 3+ analysis techniques | ✅ |
| 5+ visualizations | ✅ |
| Complete documentation | ✅ |
| Executive Summary | ✅ |
| Technical Report | ✅ |
| 10–15 slide Presentation | ✅ |
| Implementation Plan | ✅ |
| Testing Evidence | ✅ |
| Reproducible Code | ✅ |

---

<div align="center">

# DATA → EVIDENCE → ACTION

### A capstone should not stop at finding patterns.

### It should explain what the business can test next.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f093fb,50:764ba2,100:667eea&height=130&section=footer" width="100%"/>

**WEEK 8 CAPSTONE • CUSTOMER CHURN & RETENTION STRATEGY**

</div>

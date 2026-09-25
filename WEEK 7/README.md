<div align="center">

# 📊 WEEK 7 | STATISTICAL BUSINESS ANALYSIS

### Turning Customer Data Into Statistical Evidence

<img src="https://img.shields.io/badge/Python-Data%20Science-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/NumPy-Statistics-013243?style=for-the-badge&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Seaborn-Visualization-4C9A8A?style=for-the-badge" />
<img src="https://img.shields.io/badge/Scikit--Learn-Regression-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
<img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />

<br><br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,50:764ba2,100:f093fb&height=180&section=header&text=STATISTICAL%20BUSINESS%20ANALYSIS&fontSize=32&fontColor=ffffff&animation=fadeIn&fontAlignY=35" width="100%"/>

</div>

---

## 🧠 PROJECT OVERVIEW

This project applies **statistical methods to a customer churn dataset** to uncover patterns, relationships, significant differences, and predictive relationships hidden inside the data.

The analysis moves beyond simple charts and averages by asking:

> **"Are these patterns statistically meaningful?"**

The project combines:

* 📌 Descriptive Statistics
* 📈 Distribution Analysis
* 🧪 Hypothesis Testing
* 🔬 Normality Testing
* 🔗 Correlation Analysis
* 📊 ANOVA
* 🎯 Confidence Intervals
* 🤖 Multiple Linear Regression
* 💡 Business Interpretation

---

<div align="center">

## 📊 DATASET SNAPSHOT

| 📦 Records | 🧩 Features | 🔥 Churn Rate |  ⏱️ Avg. Tenure  | 💳 Avg. Monthly Charges |
| :--------: | :---------: | :-----------: | :--------------: | :---------------------: |
|   **500**  |    **9**    |   **10.6%**   | **36.53 months** |       **$113.64**       |

</div>

---

## 🗂️ PROJECT STRUCTURE

```text
WEEK 7/
│
├── 📓 statistical_analysis.ipynb
│
├── 📄 business_data.csv
│
├── 📑 statistical_report.pdf
│
├── 📊 descriptive_statistics.csv
├── 🧪 hypothesis_tests_results.txt
├── 🔬 normality_tests.csv
├── 🔗 correlation_matrix.csv
├── 📐 confidence_intervals.csv
├── 📈 regression_coefficients.csv
├── 📋 regression_summary.txt
├── 💡 business_insights.txt
│
├── 📁 visualizations/
│   ├── distribution plots
│   ├── correlation plots
│   ├── hypothesis-testing visuals
│   └── regression visuals
│
└── ⚙️ requirements.txt
```

---

# 🔬 STATISTICAL PIPELINE

<div align="center">

```text
┌───────────────────┐
│   CUSTOMER DATA   │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ DATA EXPLORATION  │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ DESCRIPTIVE STATS │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ NORMALITY TESTING │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│    CORRELATION    │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ HYPOTHESIS TESTS  │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│      ANOVA        │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ CONFIDENCE INTERVAL│
└─────────┬─────────┘
          ↓
┌───────────────────┐
│    REGRESSION     │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ BUSINESS INSIGHTS │
└───────────────────┘
```

</div>

---

# 📐 METHODS USED

### 01. 📊 DESCRIPTIVE STATISTICS

Calculated:

* Mean
* Median
* Standard deviation
* Minimum
* Maximum
* Quartiles
* Variance
* Distribution summaries

These statistics establish the numerical foundation of the dataset.

---

### 02. 📈 DISTRIBUTION ANALYSIS

The project examines variable distributions using:

* Histograms
* Density plots
* Distribution comparisons
* Outlier inspection

This helps understand the shape and spread of important business variables.

---

### 03. 🔬 NORMALITY TESTING

**Shapiro-Wilk tests** were used to investigate whether numerical variables follow an approximately normal distribution.

```text
Data
 │
 ├── Approximately Normal
 │        ↓
 │   Parametric Methods
 │
 └── Non-Normal
          ↓
     Interpret Carefully
```

---

### 04. 🔗 PEARSON CORRELATION

Pearson correlation was used to measure linear relationships between numerical variables.

One notable relationship:

```text
TENURE  ────────────────────────►  CHURN

        r ≈ -0.509
```

This indicates a **moderate negative linear association** in this dataset.

> ⚠️ Correlation does not establish causation.

---

### 05. 🧪 HYPOTHESIS TESTING

Two Welch independent-samples t-tests were performed.

#### Monthly Charges vs Churn

```text
p ≈ 0.0101
```

The result provides statistical evidence of a difference in mean monthly charges between churn groups at the 5% significance level.

#### Tenure vs Churn

```text
p ≈ 8.98 × 10⁻¹³⁰
```

The test provides very strong statistical evidence of a difference in mean tenure between churn groups.

---

### 06. 📊 ONE-WAY ANOVA

Monthly charges were compared across contract categories.

```text
ANOVA p ≈ 0.969
```

Within this dataset, the analysis does not provide statistical evidence of a difference in mean monthly charges across the contract groups.

---

### 07. 🎯 CONFIDENCE INTERVAL

A 95% confidence interval was calculated for the mean monthly charge.

```text
┌──────────────────────────────────────────┐
│        95% CONFIDENCE INTERVAL           │
│                                          │
│       $109.08  ─────────  $118.19        │
│                  ↑                       │
│             Sample Mean                  │
│                                          │
└──────────────────────────────────────────┘
```

---

### 08. 🤖 MULTIPLE LINEAR REGRESSION

A regression model was developed using:

**Target**

```text
TotalCharges
```

**Predictors**

```text
Tenure
MonthlyCharges
```

Model result:

```text
R² ≈ 0.002
```

This indicates that these predictors explain very little of the variation in `TotalCharges` within this particular dataset.

---

# 📊 KEY FINDINGS

<div align="center">

| Finding                   |        Result       |
| :------------------------ | :-----------------: |
| 👥 Dataset Size           |  **500 customers**  |
| 🔥 Churn Rate             |      **10.6%**      |
| ⏱️ Mean Tenure            |   **36.53 months**  |
| 💳 Mean Monthly Charges   |     **$113.64**     |
| 🔗 Tenure ↔ Churn         |    **r ≈ -0.509**   |
| 🧪 Monthly Charges t-test |    **p ≈ 0.0101**   |
| 🧪 Tenure t-test          | **p ≈ 8.98×10⁻¹³⁰** |
| 📊 Contract ANOVA         |    **p ≈ 0.969**    |
| 📐 Regression R²          |     **≈ 0.002**     |

</div>

---

# 💡 BUSINESS INTERPRETATION

### 🔥 CUSTOMER CHURN

The dataset has a **10.6% churn rate**, meaning approximately one in ten customers in this sample are classified as churned.

---

### ⏱️ TENURE MATTERS

The negative correlation between tenure and churn indicates that customers with longer tenure tend to have lower churn values in this dataset.

This relationship should be investigated further with additional customer and behavioral variables before drawing causal conclusions.

---

### 💳 MONTHLY CHARGES

The Welch t-test suggests a statistically significant difference in average monthly charges between churn groups.

This makes monthly charges a potentially useful variable for further churn analysis.

---

### 📑 CONTRACT TYPE

The ANOVA result does not provide evidence of a statistically significant difference in mean monthly charges across the contract groups represented in this dataset.

---

### 🤖 REGRESSION LIMITATION

The regression model produced a very low R².

This suggests that **Tenure and MonthlyCharges alone are insufficient to explain TotalCharges** in this dataset.

A stronger model would require additional explanatory variables.

---

# ⚠️ DATASET LIMITATION

The supplied files are **500-row customer churn datasets**.

They do **not** contain:

```text
❌ Marketing Spend
❌ Advertising Spend
❌ Sales Revenue
❌ Campaign Cost
❌ ROI
```

Therefore, a genuine:

```text
MARKETING SPEND
        ↓
    REVENUE
        ↓
       ROI
```

analysis cannot be performed without introducing data that does not exist in the supplied dataset.

No artificial values were created to fill this gap.

---

# 🛠️ TECHNOLOGY STACK

<div align="center">

|        Technology       | Purpose                   |
| :---------------------: | :------------------------ |
|      🐍 **Python**      | Statistical analysis      |
|      🐼 **Pandas**      | Data manipulation         |
|       🔢 **NumPy**      | Numerical computation     |
|    📊 **Matplotlib**    | Visualization             |
|      🎨 **Seaborn**     | Statistical visualization |
|   🤖 **Scikit-learn**   | Regression                |
|       🧪 **SciPy**      | Statistical testing       |
| 📓 **Jupyter Notebook** | Interactive analysis      |

</div>

---

# 🚀 SETUP & EXECUTION

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Launch Jupyter Notebook

```bash
jupyter notebook statistical_analysis.ipynb
```

### 3️⃣ Run the analysis

Execute the notebook cells sequentially to reproduce the statistical analysis and visualizations.

---

# 📚 OUTPUTS

The project generates a complete statistical evidence package:

```text
📊 Descriptive Statistics
        ↓
🔬 Normality Tests
        ↓
🔗 Correlation Matrix
        ↓
🧪 Hypothesis Tests
        ↓
📐 Confidence Intervals
        ↓
📈 Regression Coefficients
        ↓
📋 Regression Summary
        ↓
💡 Business Insights
        ↓
📑 Statistical Report
```

---

# 🎯 LEARNING OUTCOMES

Through this project, the following concepts were practiced:

* Statistical thinking for business problems
* Descriptive statistics
* Probability distributions
* Normality testing
* Pearson correlation
* Welch's t-test
* One-way ANOVA
* Confidence intervals
* Linear regression
* Statistical significance
* Business interpretation
* Responsible interpretation of limited datasets

---

# 🌟 PROJECT PHILOSOPHY

<div align="center">

### DATA → EVIDENCE → INSIGHT → DECISION

<br>

**Don't just ask what happened.**

### Ask whether the evidence supports it.

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f093fb,50:764ba2,100:667eea&height=140&section=footer" width="100%"/>

### 📊 WEEK 7 COMPLETE

**Developer's Arena | Statistical Business Analysis**

<br>

Made with 🐍 Python • 📊 Statistics • 🧠 Curiosity

</div>

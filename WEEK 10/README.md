# Customer Churn Prediction - Week 10

This project focuses on predicting customer churn using a structured customer dataset. It covers data validation, preprocessing, feature engineering, model training, and evaluation.

## Overview
# 🎯 WEEK 10 | CUSTOMER CHURN PREDICTION

### Machine Learning • Customer Analytics • Predictive Modeling

<p align="center">
  <strong>Predict Customer Churn. Understand Customer Behavior. Support Better Retention Decisions.</strong>
</p>

---

## 📌 PROJECT OVERVIEW

An end-to-end machine learning project focused on predicting customer churn using customer data, data preprocessing, feature engineering, model development, and performance evaluation.

Customer churn occurs when customers stop using a company's products or services. Identifying potential churn helps businesses understand customer behavior and develop more effective retention strategies.

### 🎯 Project Objectives

- 🔍 Explore and validate customer data.
- 🧹 Prepare data for machine learning.
- ⚙️ Perform feature engineering.
- 🤖 Develop a customer churn prediction pipeline.
- 📊 Evaluate model performance using appropriate metrics.
- 📑 Document preprocessing, validation, and evaluation results.

---

## 📂 DATASET

**Dataset file:** `churn_data.csv`

The dataset is used to explore customer characteristics and build a predictive workflow for identifying potential churn.

- **Data source:** Included project dataset
- **Target:** Customer churn
- **Task:** Classification, provided the target represents churn categories
- **Data validation:** `dataset_validation.json`
- **Outlier analysis:** `outlier_report.csv`

> The dataset's exact row count, column count, target encoding, and class distribution should be confirmed from the supplied CSV and notebook rather than assumed.

---

## 🧠 MACHINE LEARNING WORKFLOW

```text
LOAD DATA
    ↓
DATA VALIDATION
    ↓
DATA PREPROCESSING
    ↓
FEATURE ENGINEERING
    ↓
MODEL TRAINING
    ↓
MODEL EVALUATION
    ↓
RESULTS & DOCUMENTATION
```

### 🔬 Technical Requirements

- ✅ Customer dataset inspection and validation
- ✅ Data preprocessing
- ✅ Feature engineering
- ✅ Machine learning pipeline
- ✅ Model evaluation and metrics
- ✅ Validation and outlier reports
- ✅ Documented workflow
- ✅ Reproducible Python environment

---

## 🛠️ TECHNOLOGIES USED

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and evaluation |
| Jupyter Notebook | Interactive analysis |
| Matplotlib / Seaborn | Visualization, where used |

See `requirements.txt` for the project's actual dependencies.

---

## 📊 MODEL EVALUATION

Model evaluation helps measure how effectively the pipeline identifies customers who may leave a service.

Depending on the implementation, relevant classification metrics include:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of predicted churn cases that are actually churn cases.
- **Recall:** Proportion of actual churn cases successfully identified.
- **F1-score:** Balance between precision and recall.
- **Confusion Matrix:** Breakdown of correct and incorrect classifications.

📄 **Evaluation results:** `model_metrics.csv`

> Actual scores should be taken from the generated evaluation files. No unverified performance figures are reported here.

---

## 📁 PROJECT STRUCTURE

```text
WEEK 10/
│
├── churn_prediction_pipeline.ipynb
├── churn_data.csv
├── Customer_Churn_Prediction_Report.pdf
│
├── dataset_validation.json
├── validation_execution.json
├── outlier_report.csv
├── model_metrics.csv
│
├── preprocessing_report.md
├── feature_engineering_documentation.md
├── requirements.txt
│
└── SCREENSHOTS/
    └── Project screenshots
```

### 📄 Key Files

| File | Description |
|---|---|
| `churn_prediction_pipeline.ipynb` | Main analysis and prediction pipeline |
| `churn_data.csv` | Customer dataset |
| `Customer_Churn_Prediction_Report.pdf` | Detailed project report |
| `model_metrics.csv` | Recorded evaluation metrics |
| `dataset_validation.json` | Dataset validation results |
| `validation_execution.json` | Validation execution output |
| `outlier_report.csv` | Outlier analysis results |
| `preprocessing_report.md` | Data preparation documentation |
| `feature_engineering_documentation.md` | Feature engineering notes |
| `SCREENSHOTS/` | Supporting project screenshots |

---

## 🚀 SETUP & INSTALLATION

### 1. Clone the Repository

```bash
git clone https://github.com/HARIESHSARAVANAN/DEVELOPER-S-ARENA-.git
cd DEVELOPER-S-ARENA-
```

### 2. Navigate to the Project

```bash
cd "WEEK 10"
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Launch the Notebook

```bash
jupyter notebook churn_prediction_pipeline.ipynb
```

Follow the notebook cells in order to execute the data preparation, modeling, and evaluation workflow.

---

## 🔮 FUTURE ENHANCEMENTS

- 📈 Compare multiple classification algorithms.
- 🎛️ Tune model hyperparameters.
- ⚖️ Investigate class imbalance and appropriate evaluation strategies.
- 🔍 Improve model interpretability.
- 🌐 Develop a web interface for churn predictions.
- 💡 Translate prediction results into customer retention recommendations.

---

## 💼 LEARNING OUTCOMES

Through this project, the workflow covers practical concepts in:

- Data preparation and validation
- Feature engineering
- Machine learning pipelines
- Classification model evaluation
- Technical documentation
- Reproducible project organization

---

## 👨‍💻 AUTHOR

**Hariesh Saravanan**

B.Tech — Artificial Intelligence and Data Science

🔗 **GitHub:** [HARIESHSARAVANAN](https://github.com/HARIESHSARAVANAN)

---

<p align="center">
  <strong>DEVELOPER'S ARENA | WEEK 10</strong><br>
  <em>Turning customer data into actionable insights.</em>
</p>


Customer churn is the rate at which customers stop using a service. In this project, the goal is to identify early indicators of churn so that business decisions can be supported with data-driven insights.

The workflow includes:

- loading and validating the dataset
- checking for missing values, duplicates, and class imbalance
- preprocessing categorical and numerical data
- engineering new predictive features
- comparing model performance
- documenting results in the repository

## Project Files

The main files in this project are:

- `churn_prediction_pipeline.ipynb` — end-to-end notebook for analysis and modeling
- `churn_data.csv` — customer dataset used for training and evaluation
- `preprocessing_report.md` — documentation of preprocessing steps
- `feature_engineering_documentation.md` — explanation of engineered features
- `model_metrics.csv` — model evaluation metrics
- `outlier_report.csv` — outlier analysis results
- `dataset_validation.json` — validation summary
- `validation_execution.json` — execution validation details
- `requirements.txt` — Python dependency list

## Folder Structure

```text
WEEK 10/
├── churn_prediction_pipeline.ipynb
├── churn_data.csv
├── dataset_validation.json
├── feature_engineering_documentation.md
├── model_metrics.csv
├── outlier_report.csv
├── preprocessing_report.md
├── requirements.txt
├── validation_execution.json
└── README.md
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/HARIESHSARAVANAN/DEVELOPER-S-ARENA-.git
cd DEVELOPER-S-ARENA-
```

2. Open the Week 10 folder:

```bash
cd "WEEK 10"
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On Git Bash / macOS / Linux:

```bash
source .venv/Scripts/activate
```

4. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Notebook

After installing the dependencies, open the notebook:

```bash
jupyter notebook churn_prediction_pipeline.ipynb
```

Run all cells in order to:

- load the dataset
- validate the schema
- inspect the data quality
- perform feature engineering
- train models
- generate evaluation outputs

## Key Notes

- `CustomerID` is excluded from model features because it is an identifier, not a behavioral predictor.
- The project compares multiple encoding methods and scaling techniques.
- Model metrics are saved in `model_metrics.csv`.
- Feature engineering and preprocessing details are documented in the accompanying markdown files.

## Model Results

The notebook records model evaluation metrics in `model_metrics.csv`. Example output from the project includes:

| Model | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest | 0.99 | 1.00 | 0.91 | 0.95 | 1.00 |
| Logistic Regression | 0.94 | 0.65 | 1.00 | 0.79 | 0.996 |

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Author

Hariesh Saravanan

## License

This project is intended for educational and academic use.

---

If you want to improve this project further, you can add:

- a web dashboard for churn prediction
- class imbalance handling
- cross-validation and hyperparameter tuning
- a deployment-ready API or model serving layer

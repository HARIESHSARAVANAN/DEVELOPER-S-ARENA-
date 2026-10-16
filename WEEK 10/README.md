# Customer Churn Prediction - Week 10

This project focuses on predicting customer churn using a structured customer dataset. It covers data validation, preprocessing, feature engineering, model training, and evaluation.

## Overview

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

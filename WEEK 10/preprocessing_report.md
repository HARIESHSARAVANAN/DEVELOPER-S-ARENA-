# Customer Churn Prediction: Preprocessing Report

## Project overview and objectives
This project explores customer churn data, preprocesses mixed-type features, engineers new variables, ranks features, and compares baseline classifiers.

### Dataset inspected
- File: `churn_data.csv`
- Rows: 500
- Columns: 9
- Columns: CustomerID, Tenure, MonthlyCharges, TotalCharges, Contract, PaymentMethod, PaperlessBilling, SeniorCitizen, Churn
- Target: `Churn`; observed values: [0, 1]
- Missing cells in source file: 0
- Duplicate rows in source file: 0

## Setup and installation
Use Python 3.10+ if possible.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```
Open `churn_prediction_pipeline.ipynb`, keep `churn_data.csv` beside it, and run all cells. If using an older scikit-learn version, upgrade with `pip install -U scikit-learn`.

## Code structure
```text
Customer-Churn-Prediction/
├── churn_prediction_pipeline.ipynb
├── churn_data.csv
├── preprocessing_report.md
├── feature_engineering_documentation.md
└── requirements.txt
```
The notebook also creates `model_metrics.csv`, `outlier_report.csv`, and (if supported) `feature_importance.csv` when executed.

## Complete preprocessing pipeline and rationale

### 1. Data validation
Inspect column types, missing values, duplicates, summary statistics, and churn balance. Drop rows with missing target labels and validate binary labels. Predictor missingness is imputed in the pipeline. This catches schema problems without fitting preprocessing on test data.

### 2. Identifier exclusion
`CustomerID` is excluded from predictors because it is an identifier and usually does not represent customer behavior.

### 3. Feature engineering
Nine features are created: `TenureYears`, `AvgHistoricalMonthlySpend`, `MonthlyToTotalRatio`, `ContractCommitmentMonths`, `IsMonthToMonth`, `HasElectronicCheck`, `PaperlessBillingFlag`, `TenureChargeInteraction`, and `HighMonthlyChargesFlag`. Details and caveats are in `feature_engineering_documentation.md`.

**Caveat:** the teaching example's `HighMonthlyChargesFlag` threshold uses the full dataset median before splitting. For strict production use, learn the threshold from training data inside a custom transformer, or omit this flag. Other learned preprocessing steps are fitted inside the pipeline.

### 4. Train/test split
A stratified 80/20 split with fixed random seed is used. Learned imputers, IQR clipping bounds, scalers, and encoders are fitted through the training pipeline only. This reduces leakage and preserves class proportions.

### 5. Categorical encoding
- **Label encoding:** demonstrated on target labels only; not used for nominal input categories.
- **One-hot encoding:** nominal `PaymentMethod` and `PaperlessBilling` categories become binary indicator columns; unseen categories are ignored.
- **Ordinal encoding:** `Contract` is ordered Month-to-month < One year < Two year.

Rationale: match encoding to category meaning and the needs of numeric models.

### 6. Imputation
Numeric features use median imputation; categorical features use most-frequent imputation. Imputation is fitted on training data through the pipeline.

### 7. Outlier detection and handling
IQR outliers are outside Q1 − 1.5×IQR or Q3 + 1.5×IQR. Z-score outliers have absolute score greater than 3. These are screening heuristics, not proof of errors. The model pipeline clips numeric extremes to training-fitted IQR fences instead of deleting potentially valid customers.

### 8. Scaling
Min-Max scaling is demonstrated separately and maps numeric features to [0, 1]. StandardScaler is used in the model pipeline to center and scale numeric values. The two scalers are compared, not stacked.

### 9. Feature selection
The notebook reports numeric correlation with target, mutual information, and Random Forest feature importance. These rankings are exploratory. Validate any feature removal with cross-validation and domain knowledge.

### 10. Modeling and evaluation
Logistic Regression and Random Forest are compared with accuracy, precision, recall, F1, ROC-AUC, confusion matrix, and classification report. The example selects by held-out F1 for demonstration; rigorous model selection should use cross-validation on training data and a final untouched test set.

## Architecture
```text
CSV → validation + feature engineering → stratified train/test split
  → ColumnTransformer
      ├─ numeric: median imputation → IQR clipping → StandardScaler
      ├─ nominal: mode imputation → OneHotEncoder
      └─ contract: mode imputation → OrdinalEncoder
  → classifier → metrics, plots, feature rankings, reports
```

## Technical requirements checklist
- [x] Three encoding methods: Label, One-Hot, Ordinal.
- [x] Two scaling techniques: Min-Max and Standard.
- [x] Five or more engineered features: nine defined.
- [x] IQR and Z-score outlier detection.
- [x] Train-fitted IQR clipping in model pipeline.
- [x] Feature ranking with correlation, mutual information, Random Forest importance.
- [x] Complete preprocessing pipeline.
- [x] Evaluation metrics and automated assertions.
- [x] Rationale for each preprocessing step.

## Screenshots of working application
Screenshots must be captured after running the notebook in Jupyter; they are not fabricated in this submission. Capture: (1) dataset preview and churn chart, (2) encoding/scaling and outlier results, (3) model metrics and confusion matrix/ROC curve, and (4) final PASS messages. Save them under `screenshots/` and embed them, for example:

```markdown
![Churn distribution](screenshots/churn_distribution.png)
![Model evaluation](screenshots/model_evaluation.png)
![Pipeline validation](screenshots/pipeline_validation.png)
```

## Testing evidence
The notebook asserts binary target validity, creation of at least five engineered features, train/test separation, finite metrics, and successful predictions including an unseen nominal category. Run all cells to produce actual test output and model metrics.

## Limitations and responsible use
This dataset has 500 rows, so metrics may vary across splits. Confirm target-label semantics with the source. Predictions should support, not replace, human decisions. Do not publish sensitive real customer data to a public repository.

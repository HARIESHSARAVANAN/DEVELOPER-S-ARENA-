# 🏠 WEEK 9 — HOUSE PRICE PREDICTION

## PROJECT OVERVIEW

An introductory machine learning project that predicts house prices using **scikit-learn**, train-test splitting, multiple regression models and evaluation metrics.

### Dataset

- **Rows:** 300
- **Columns:** 8
- **Target:** Price
- **Features:** Area, Bedrooms, Bathrooms, Age, Location, Property Type

## MODELS

1. Linear Regression from scratch
2. Scikit-learn Linear Regression
3. Polynomial Regression
4. Decision Tree Regressor
5. Random Forest Regressor

## TECHNICAL REQUIREMENTS

- ✅ scikit-learn implementation
- ✅ Proper 80/20 train-test split
- ✅ MAE
- ✅ MSE
- ✅ RMSE
- ✅ R²
- ✅ Actual vs predicted visualization
- ✅ Model comparison
- ✅ Model evaluation report
- ✅ Feature interpretation

## PROJECT STRUCTURE

```text
WEEK 9/
├── house_price_prediction.ipynb
├── house_data.csv
├── model_evaluation_report.md
├── requirements.txt
├── predictions_vs_actual.png
├── residual_analysis.png
├── model_comparison.png
├── predictions.csv
├── model_metrics.csv
└── linear_regression_from_scratch.md
```

## SETUP

```bash
pip install -r requirements.txt
jupyter notebook house_price_prediction.ipynb
```

## EXPECTED WORKFLOW

**LOAD → CLEAN → SPLIT → TRAIN → EVALUATE → VISUALIZE → INTERPRET**

## DATA QUALITY

The supplied dataset contains no missing values, so no artificial values were imputed.

## IMPORTANT

The example MAE and R² values in the assignment brief are illustrative. This project reports the metrics calculated from the supplied `house_prices.csv` dataset.

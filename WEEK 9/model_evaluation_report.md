# WEEK 9 — MODEL EVALUATION REPORT

## PROJECT OVERVIEW

This project builds a machine learning system to predict house prices from property characteristics. The supplied dataset contains **300 rows and 8 columns**.

### Objective

Predict `Price` using:

- Area
- Bedrooms
- Bathrooms
- Age
- Location
- Property Type

## DATA QUALITY

- Rows: **300**
- Columns: **8**
- Missing values: **0**
- Target: **Price**
- Train/test split: **80% / 20%**
- Random state: **42**

## METHODS

### 1. Linear Regression From Scratch

A one-variable least-squares regression was implemented using Area to demonstrate the mathematical foundation of linear regression.

### 2. Scikit-learn Linear Regression

A complete preprocessing pipeline was used with numeric scaling and one-hot encoding for categorical variables.

### 3. Polynomial Regression

Degree-2 polynomial features were added to the numeric variables to capture nonlinear relationships.

### 4. Decision Tree Regressor

A constrained decision tree was tested as a nonlinear baseline.

### 5. Random Forest Regressor

An ensemble of 300 decision trees was trained to capture nonlinear relationships and interactions.

## MODEL PERFORMANCE

| Model | MAE | MSE | RMSE | R² |
|---|---:|---:|---:|---:|
| Random Forest Regressor | $1,463,090.80 | $3,917,323,301,006.09 | $1,979,222.90 | 0.9725 |
| Linear Regression | $2,188,736.34 | $8,454,330,868,276.76 | $2,907,633.21 | 0.9406 |
| Decision Tree Regressor | $2,491,788.26 | $9,603,066,771,952.24 | $3,098,881.54 | 0.9326 |
| Polynomial Regression (Degree 2) | $2,367,902.24 | $10,116,153,889,350.56 | $3,180,590.18 | 0.9290 |

## BEST MODEL

The best test-set R² among the evaluated models is **Random Forest Regressor**, with R² = **0.9725**.

## INTERPRETATION

MAE represents the average absolute prediction error in the dataset's price units. RMSE penalizes larger errors more heavily than MAE. R² represents the proportion of target variance explained by the model on the test set.

The best model should not be selected solely because it has the highest R². Model complexity, generalization, interpretability and future validation should also be considered.

## VISUAL VALIDATION

The project includes:

- `predictions_vs_actual.png` — actual versus predicted prices
- `residual_analysis.png` — residual behavior
- `model_comparison.png` — R² comparison across models

## BUSINESS INSIGHTS

1. **Area is expected to be an important pricing signal** because larger properties generally provide more usable space.
2. **Location can materially affect price**, which is why categorical encoding is included.
3. **Bedrooms and bathrooms add property-level context** beyond raw area.
4. **Property age may influence valuation**, potentially capturing depreciation or property condition.
5. **Tree-based models can capture nonlinear interactions** that a simple linear model may miss.

## LIMITATIONS

- The dataset contains only 300 properties.
- Location categories are limited to the supplied dataset.
- No transaction date, neighborhood-level pricing, amenities, land value, renovation status or market trend variables are included.
- Test-set performance should not be treated as a guaranteed production performance level.

## CONCLUSION

The project demonstrates the complete introductory machine-learning workflow: data inspection, preprocessing, train-test splitting, baseline modeling, nonlinear model comparison, evaluation with multiple metrics and visualization of predictions versus actual values.

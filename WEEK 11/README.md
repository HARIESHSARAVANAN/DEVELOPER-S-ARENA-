# Week 11: Customer Segmentation & Prediction

## Overview
A reproducible machine-learning capstone comparing K-Means, Agglomerative clustering and DBSCAN, then training segment-specific Random Forest churn classifiers with hyperparameter tuning and comprehensive metrics.

## Dataset
The uploaded CSV contains 500 rows and 9 columns: CustomerID, Tenure, MonthlyCharges, TotalCharges, Contract, PaymentMethod, PaperlessBilling, SeniorCitizen and Churn. The task brief mentions 4 columns, but this supplied file has 9. Churn is the binary target; CustomerID is excluded from features.

## Repository structure
- `customer_segmentation.ipynb`: full analysis and training workflow
- `segmentation_data.csv`: supplied data with SegmentID and SegmentName appended
- `segment_profiles.md` / `segment_profiles.csv`: customer profiles
- `model_evaluation_results.csv`: per-segment metrics and best parameters
- `business_recommendations.pdf`: business interpretation and actions
- `screenshots/`: generated analysis charts

## Setup
1. Install Python 3.10+.
2. Optional virtual environment: `python -m venv .venv`
3. Activate it: Windows `.venv\\Scripts\\activate`; macOS/Linux `source .venv/bin/activate`
4. Install: `pip install -r requirements.txt`
5. Launch: `jupyter notebook`
6. Open `customer_segmentation.ipynb` and run all cells.

## Technical requirements
- 3 clustering algorithms: K-Means, Agglomerative, DBSCAN.
- 3 K-Means segments for downstream segment-specific classifiers.
- Random Forest with GridSearchCV over estimator count, depth and leaf size, when class counts permit.
- Accuracy, precision, recall, F1 and ROC-AUC when valid.
- Elbow analysis, silhouette comparisons, segment profiles, visualizations and business recommendations.
- Overfitting controls: held-out testing, cross-validation, depth/leaf tuning and honest handling of small segments.

## Validation and limitations
The workflow checks dimensions, missingness, duplicates and class distribution. Churn is excluded from clustering to prevent leakage. Segment-level metrics may be unstable due to small sample sizes; ROC-AUC is omitted if a test split contains one class. DBSCAN may label observations as noise and is sensitive to its parameters. Business impact is not claimed as measured uplift; validate recommendations using controlled tests.

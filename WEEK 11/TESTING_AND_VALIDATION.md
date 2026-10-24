# Testing and Validation Evidence

## Dataset checks
- Loaded the supplied CSV successfully.
- Observed 500 rows and 9 columns in the supplied file.
- Checked missing values and duplicate rows.
- Excluded `CustomerID` from model features.
- Excluded `Churn` from clustering features to prevent target leakage.

## Clustering checks
- Implemented K-Means and inspected inertia across k=2..6 using the Elbow method.
- Implemented Agglomerative (hierarchical) clustering with three clusters.
- Implemented DBSCAN and compared cluster counts, noise points, and silhouette scores.
- Created customer profiles from K-Means assignments.

## Prediction checks
- Trained a separate Random Forest pipeline for each of the three K-Means segments when sample size and target classes allowed.
- Used train/test splits and GridSearchCV to tune `n_estimators`, `max_depth`, and `min_samples_leaf` where there were enough minority-class examples for cross-validation.
- Calculated accuracy, precision, recall, F1-score, and ROC-AUC when the metric was valid.
- Metrics are reported from held-out test data; small test sets can make results unstable.

## Key limitation observed
The Long-Tenure Value segment model achieved about 89.7% accuracy but 0.0 recall on its held-out split. This means it missed churners in that test split. Do not judge the model by accuracy alone; investigate class imbalance, threshold selection, and additional validation before business use.

## Visual evidence
The `screenshots/` folder contains generated output charts for the Elbow method, segment sizes, churn rates by segment, and clustering algorithm comparison. These are analysis visuals, not screenshots of a deployed web application. The deliverable is a Jupyter Notebook project, and no separate web application was specified.

## Reproducibility
Install dependencies from `requirements.txt`, open `customer_segmentation.ipynb`, and run all cells in order. The notebook expects `segmentation_data.csv` in the same directory. Outputs may vary slightly across software versions.

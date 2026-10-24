# Customer Segment Profiles

## Methodology
CustomerID and Churn were excluded from clustering to avoid target leakage. Numeric fields were median-imputed and standardized; categorical fields were mode-imputed and one-hot encoded. K-Means with three clusters supplies the segments for separate prediction models. Hierarchical clustering and DBSCAN are compared as alternatives.

## Segment 0: Long-Tenure Value
- Customers: 114 (22.8%)
- Average Tenure: 39.54
- Average MonthlyCharges: 97.83
- Average TotalCharges: 6239.81
- Average SeniorCitizen: 0.0
- Churn rate: 8.8%
- Most common Contract: One year
- Most common PaymentMethod: Credit Card
- Most common PaperlessBilling: No

## Segment 1: Developing / Mixed
- Customers: 249 (49.8%)
- Average Tenure: 35.7
- Average MonthlyCharges: 108.14
- Average TotalCharges: 4274.98
- Average SeniorCitizen: 1.0
- Churn rate: 10.0%
- Most common Contract: Month-to-month
- Most common PaymentMethod: Credit Card
- Most common PaperlessBilling: No

## Segment 2: Newer High-Charge
- Customers: 137 (27.4%)
- Average Tenure: 35.54
- Average MonthlyCharges: 136.77
- Average TotalCharges: 2504.63
- Average SeniorCitizen: 0.0
- Churn rate: 13.1%
- Most common Contract: One year
- Most common PaymentMethod: Electronic Check
- Most common PaperlessBilling: Yes

## Business implications
- **Established High-Value:** prioritize loyalty, proactive service recovery and relevant upgrades; avoid blanket discounts.
- **Newer High-Charge:** strengthen onboarding, clarify plan value and investigate early billing/service friction.
- **Long-Tenure Value:** reward loyalty and test relevant bundles while protecting margin.
- **Developing / Mixed:** use controlled experiments rather than assuming all customers in the segment behave alike.

These names are heuristic, not causal or permanent labels. Validate with domain experts. Business impact must be tested with controlled experiments.

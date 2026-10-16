# Feature Engineering Documentation

## Purpose
Feature engineering derives useful representations from customer predictors. No feature below uses `Churn`.

| Feature | Formula / rule | Rationale | Caveat |
|---|---|---|---|
| `TenureYears` | `Tenure / 12` | Expresses tenure in years. | Assumes tenure is measured in months. |
| `AvgHistoricalMonthlySpend` | `TotalCharges / Tenure`; zero tenure becomes missing | Approximate historical monthly spend. | May be noisy if charges include fees, discounts, or incomplete billing. |
| `MonthlyToTotalRatio` | `MonthlyCharges / (abs(TotalCharges) + 1)` | Relates recurring charges to accumulated charges. | The +1 prevents division by zero; not a formal financial metric. |
| `ContractCommitmentMonths` | Month-to-month → 1; One year → 12; Two year → 24 | Numeric proxy for commitment length. | Month-to-month is not necessarily a literal one-month fixed contract. |
| `IsMonthToMonth` | 1 if contract is Month-to-month, else 0 | Explicitly represents the flexible-contract group. | May be redundant with encoded contract type. |
| `HasElectronicCheck` | 1 if payment method is Electronic Check, else 0 | Captures payment behavior. | Association does not imply causation. |
| `PaperlessBillingFlag` | Yes → 1; No → 0 | Numeric billing preference. | Unknown values are imputed downstream. |
| `TenureChargeInteraction` | `Tenure × MonthlyCharges` | Represents combined tenure/charge effects. | May correlate with other features. |
| `HighMonthlyChargesFlag` | 1 if monthly charges are at least the dataset median, else 0 | Creates a high/low charge segment. | In this teaching notebook, median is computed before split; production threshold should be learned from training data inside a transformer. |

## Implementation
The `engineer_features(frame)` function in the notebook creates these columns in a copy of the input frame and preserves the source columns. Missing values are handled by pipeline imputers.

## Validation recommendations
1. Confirm units and definitions with the data provider.
2. Inspect distributions and missingness for each derived feature.
3. Check correlation and mutual information for redundancy.
4. Compare model performance with and without each feature using cross-validation.
5. Keep feature creation identical at training and inference.
6. Never use target labels to construct predictors.

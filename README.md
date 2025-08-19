# Loan Default Analysis

## Project Overview
Analyze LendingClub loan data to explore factors affecting loan defaults.

## Data
- Source: LendingClub (2007 accepted loans)
- Key columns: loan amount, interest rate, employment length, credit grade, purpose, etc.

## Data Cleaning
- Removed rows with missing critical values.
- Converted `term` to numeric.
- Standardized `emp_length`.
- Converted `revol_util` to numeric.
- Created a `default` column (1 if Charged Off / Default / Late, 0 otherwise).

## Exploratory Data Analysis
- Default distribution and rate.
- Distribution of numeric features.
- Default rate by grade, term, and purpose.
- Correlation analysis.

## Scripts
- `scripts/data_cleaning.py` – main cleaning and EDA script.

## Next Steps
- Predictive modeling of loan defaults.
- Interactive visualization with Power BI.

## Requirements
```bash
pip install -r requirements.txt

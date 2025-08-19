# Loan Default Analysis

This project explores Lending Club loan data to understand factors that influence loan defaults. It includes **data cleaning, feature engineering, exploratory data analysis (EDA), and visualizations**.

---

## Dataset

The dataset used in this project is publicly available on Kaggle:

[Lending Club Loan Data (2007-2018)](https://www.kaggle.com/datasets/wordsforthewise/lending-club?select=accepted_2007_to_2018Q4.csv.gz)

**Note:** The raw dataset is **not included** in this repository due to size. After downloading from Kaggle, place the relevant CSV file in the `data/` folder.

---

## Project Structure


---

## Features Processed

The project processes and analyzes these key features:

- Loan amount (`loan_amnt`)
- Loan term (`term`)
- Interest rate (`int_rate`)
- Installment amount (`installment`)
- Credit grade (`grade`, `sub_grade`)
- Employment length (`emp_length`)
- Home ownership (`home_ownership`)
- Annual income (`annual_inc`)
- Debt-to-income ratio (`dti`)
- Revolving credit utilization (`revol_util`)
- Loan purpose (`purpose`)
- State of residence (`addr_state`)
- Credit history (`delinq_2yrs`, `inq_last_6mths`, `open_acc`, `pub_rec`, `total_acc`)
- Loan status and default indicator

---

## How to Use

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/Loan_Default_Analysis.git
cd Loan_Default_Analysis

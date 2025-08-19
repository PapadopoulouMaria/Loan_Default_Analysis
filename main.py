import pandas as pd
df = pd.read_csv('/Users/mariapapadopoulou/Documents/acceptedLoans/accepted_2007.csv', on_bad_lines='skip',
                 low_memory=False)
print(df.head())
selected_cols = [
    'member_id', 'loan_amnt', 'term', 'int_rate', 'installment', 'grade', 'sub_grade',
    'emp_length', 'home_ownership', 'annual_inc', 'verification_status',
    'purpose', 'addr_state', 'dti', 'delinq_2yrs', 'inq_last_6mths',
    'open_acc', 'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'loan_status'
]
df = df[selected_cols]

df.drop(columns=['member_id'], inplace=True)
df.dropna( subset=[
    'loan_amnt', 'term', 'int_rate', 'installment', 'grade', 'sub_grade',
    'emp_length', 'home_ownership', 'annual_inc', 'verification_status',
    'purpose', 'addr_state', 'dti', 'delinq_2yrs', 'inq_last_6mths',
    'open_acc', 'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'loan_status'
], inplace=True)
df['term'] = df['term'].str.extract(r'(\d+)').astype(int)
def clean_emp_length(val):
    """Convert employment length text to numeric years."""
    if pd.isnull(val):
        return None
    elif '<' in val:
        return 0
    elif '10+' in val:
        return 10
    else:
        return int(str(val).split()[0])
df['emp_length'] = df['emp_length'].apply(clean_emp_length)

df['revol_util'] = df['revol_util'].astype(str).str.replace('%', '', regex=False)
df['revol_util'] = pd.to_numeric(df['revol_util'], errors='coerce')

default_values = ['Charged Off', 'Default', 'Late (31-120 days)']

df['default'] = df['loan_status'].apply(lambda x: 1 if x in default_values else 0)

df.reset_index(drop=True, inplace=True)

print(df.info())
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

default_rate = df['default'].mean()
print(f'Default rate: {default_rate:.2%}')

sns.countplot(data=df, x='default')
plt.title('Loan Default vs Non-default')
plt.xticks([0, 1], ['Non-default', 'Default'])
plt.show()

num_features = ['loan_amnt', 'int_rate', 'annual_inc', 'dti', 'revol_util']

for col in num_features:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], bins=40, kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='grade', y='default')
plt.title('Default Rate by Credit Grade')
plt.show()

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='term', y='default')
plt.title('Default Rate by Loan Term')
plt.show()

plt.figure(figsize=(12, 5))
sns.barplot(data=df, x='purpose', y='default')
plt.title('Default Rate by Loan Purpose')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

df.to_csv('cleaned_loan_data.csv', index=False)

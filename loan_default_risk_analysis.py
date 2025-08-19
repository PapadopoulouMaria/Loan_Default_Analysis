# Loan Default Risk Analysis - Data Cleaning & EDA
# Author: Maria Papadopoulou
# Date: 2025
# Description:
# Script to clean Lending Club loan data, perform basic EDA,
# and export the cleaned dataset for further analysis (e.g. Power BI, modeling).

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
def load_data(filepath):
    df = pd.read_csv(filepath, on_bad_lines='skip', low_memory=False)
    return df


# Keep only relevant columns
def select_and_clean_columns(df):
    selected_cols = [
        'member_id', 'loan_amnt', 'term', 'int_rate', 'installment', 'grade', 'sub_grade',
        'emp_length', 'home_ownership', 'annual_inc', 'verification_status',
        'purpose', 'addr_state', 'dti', 'delinq_2yrs', 'inq_last_6mths',
        'open_acc', 'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'loan_status'
    ]
    df = df[selected_cols]
    df.drop(columns=['member_id'], inplace=True)

    # Drop rows with missing values
    df.dropna(subset=selected_cols[1:], inplace=True)

    # Convert term to numeric
    df['term'] = df['term'].str.extract(r'(\d+)').astype(int)

    # Clean employment length
    df['emp_length'] = df['emp_length'].apply(clean_emp_length)

    # Convert revol_util to numeric
    df['revol_util'] = df['revol_util'].astype(str).str.replace('%', '', regex=False)
    df['revol_util'] = pd.to_numeric(df['revol_util'], errors='coerce')

    # Create default column (1 = risky, 0 = safe)
    default_values = ['Charged Off', 'Default', 'Late (31-120 days)']
    df['default'] = df['loan_status'].apply(lambda x: 1 if x in default_values else 0)

    df.reset_index(drop=True, inplace=True)
    return df


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


def plot_default_distribution(df):
    default_rate = df['default'].mean()
    print(f'Default rate: {default_rate:.2%}')

    sns.countplot(data=df, x='default')
    plt.title('Loan Default vs Non-default')
    plt.xticks([0, 1], ['Non-default', 'Default'])
    plt.show()


# Distributions of numeric features
def plot_numeric_distributions(df, num_features):
    for col in num_features:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col], bins=40, kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()


# Default by grade
def plot_categorical_analysis(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='grade', y='default')
    plt.title('Default Rate by Credit Grade')
    plt.show()

    # Default by term
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df, x='term', y='default')
    plt.title('Default Rate by Loan Term')
    plt.show()

    # Default by purpose
    plt.figure(figsize=(12, 5))
    sns.barplot(data=df, x='purpose', y='default')
    plt.title('Default Rate by Loan Purpose')
    plt.xticks(rotation=45)
    plt.show()


# Correlation matrix
def plot_correlation_matrix(df):
    plt.figure(figsize=(12, 8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()


def main():
    filepath = '/Users/mariapapadopoulou/Documents/acceptedLoans/accepted_2007.csv'
    df = load_data(filepath)

    print(df.head())

    df = select_and_clean_columns(df)

    print(df.info())
    print(df.head())

    # Exploratory Analysis
    plot_default_distribution(df)
    num_features = ['loan_amnt', 'int_rate', 'annual_inc', 'dti', 'revol_util']
    plot_numeric_distributions(df, num_features)
    plot_categorical_analysis(df)
    plot_correlation_matrix(df)

    # Save cleaned data
    df.to_csv('cleaned_loan_data.csv', index=False)


if __name__ == "__main__":
    main()

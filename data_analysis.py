import pandas as pd

def average_monthly_spending(df):
    # print(df)
    monthly_spending = df[df['Type'].isin(['Expense'])]
    # print(monthly_spending)
    monthly_spending['Date'] = pd.to_datetime(monthly_spending['Date'])
    month = monthly_spending['Date'].dt.to_period('M')
    average_spending = monthly_spending.groupby(month)['Amount'].mean()
    print("--- Average Monthly Spending ---")
    print(average_spending)
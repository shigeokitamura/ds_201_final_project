import matplotlib.pyplot as plt

def monthly_spending_trend(df):
    df[['Year','Month','Day']] = df['Date'].str.split('-', expand= True)
    spending = df[df['Category'] != 'Income']
    spending.groupby('Month')['Amount'].plot(kind='line')

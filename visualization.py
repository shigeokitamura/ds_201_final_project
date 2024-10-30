import matplotlib.pyplot as plt

def monthly_spending_trend(df):
    df[['Year','Month','Day']] = df['Date'].str.split('-', expand= True)
    print(df)
    spending = df[df['Type'] == 'Expense']
    spending.groupby('Month')['Amount'].sum().plot(kind='line')
    plt.xlabel('month')
    plt.ylabel('spending')
    plt.show()

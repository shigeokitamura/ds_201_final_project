import matplotlib.pyplot as plt

def monthly_spending_trend(df):
    df[['Year','Month','Day']] = df['Date'].str.split('-', expand= True)
    spending = df[df['Type'] == 'Expense']
    spending.groupby('Month')['Amount'].sum().plot(kind='line')
    plt.xlabel('month')
    plt.ylabel('spending')
    plt.title('Monthly Spending Trend')
    plt.show()

def spending_by_category(df):
    spending = df[df['Type'] == 'Expense']
    total_by_category = spending.groupby('Category')['Amount'].sum()
    total_by_category.plot(kind='bar')
    plt.xlabel('Category')
    plt.ylabel('amount of spending')
    plt.title('Spending By Category')
    plt.show()

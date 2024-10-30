import matplotlib.pyplot as plt
import data_management

def monthly_spending_trend(df):
    df[['Year','Month','Day']] = df['Date'].str.split('-', expand= True)
    spending = df[df['Type'] == 'Expense']
    spending.groupby('Month')['Amount'].sum().plot(kind='line')
    plt.xlabel('month')
    plt.ylabel('spending')
    plt.show()

def spending_by_category(df):
    spending = df[df['Type'] == 'Expense']
    total_by_category = spending.groupby('Category')['Amount'].sum()
    total_by_category.plot(kind='bar')
    plt.xlabel('Category')
    plt.ylabel('amount of spending')
    plt.show()
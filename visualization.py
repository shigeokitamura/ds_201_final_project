import matplotlib.pyplot as plt

def monthly_spending_trend(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

    df[['Year','Month','Day']] = df['Date'].str.split('-', expand= True)
    spending = df[df['Type'] == 'Expense']
    spending.groupby('Month')['Amount'].sum().plot(kind='line')
    plt.xlabel('month')
    plt.ylabel('spending')
    plt.title('Monthly Spending Trend')
    plt.show()

def spending_by_category(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

    spending = df[df['Type'] == 'Expense']
    total_by_category = spending.groupby('Category')['Amount'].sum()
    total_by_category.plot(kind='bar')
    plt.xlabel('Category')
    plt.ylabel('amount of spending')
    plt.title('Spending By Category')
    plt.show()

def distribution_of_spending_by_categories(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

    spending = df[df['Type'] == 'Expense']
    dis_spending_categories = spending.groupby('Category')['Amount'].sum()
    dis_spending_categories.plot(kind='pie', subplots=True, autopct='%1.0f%%', title ='The Distribution of Spending across Categories')
    plt.show()

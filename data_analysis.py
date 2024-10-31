import pandas as pd
import visualization

def average_monthly_spending(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

    monthly_spending = df[df['Type'].isin(['Expense'])].copy()
    monthly_spending['Date'] = pd.to_datetime(monthly_spending['Date'])
    month = monthly_spending['Date'].dt.to_period('M')
    average_spending = monthly_spending.groupby(month)['Amount'].mean()
    print()
    print("--- Average Monthly Spending ---")
    print(average_spending)
    print()


def analyze_spending_by_category(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

    total_spending = making_total_spending_data_frame(df)
    print()
    print('--- This is total spending for each category. ---')
    print(total_spending)
    print()

    while True:
        user = input('Do you want to see pie chart representing the distribution of spending across categories? (Yes/No): ')
        if user.lower() in ['yes','y']:
            visualization.distribution_of_spending_by_categories(df)
            print()
            break
        elif user.lower() in ['no', 'n']:
            print('Back to the menus')
            print()
            break
        else:
            print("Follow the format (Yes/No): ")
            print()


def making_total_spending_data_frame(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

    df = df[df['Type'] == 'Expense']
    total_spending = df.groupby('Category')['Amount'].sum()
    # set the column name
    total_spending = total_spending.reset_index()
    total_spending.columns = ['Category', 'Total_Spending']
    return total_spending


def top_spending_category(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

    total_spending = making_total_spending_data_frame(df)
    total_spending = total_spending[total_spending['Category'] != 'Income']
    print()
    print('--- This is the highest total spending with category. ---')
    print(total_spending.loc[total_spending['Total_Spending'] == total_spending['Total_Spending'].max()])
    print()


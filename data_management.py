from datetime import datetime
import matplotlib.pyplot as plt


def view_all_trans(df):
    print()
    print(df)
    print()

def view_trans_by_date_range(df):
    while True:
        try:
            start_date = input("write down the specific start date which you want to see (YYYY-MM-DD):")
            datetime.strptime(start_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("You should follow this format using number(YYYY-MM-DD).")

    while True:
            try:
                end_date = input("write down the specific end date which you want to see (YYYY-MM-DD):")
                datetime.strptime(end_date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("You should follow this format using number(YYYY-MM-DD).")

    range_date = df[(df['Date'] > start_date) & (df['Date'] < end_date)]
    print()
    print(range_date)
    print()

def making_total_spending_data_frame(df):
    total_spending = df.groupby('Category')['Amount'].sum()
    # set the column name
    total_spending = total_spending.reset_index()
    total_spending.columns = ['Category', 'Total_Spending']
    return total_spending

def analyze_spending_by_category(df):
    total_spending = making_total_spending_data_frame(df)
    print()
    print(f'This is total spending for each category.')
    print(total_spending)
    print()

def top_spending_category(df):
    total_spending = making_total_spending_data_frame(df)
    total_spending = total_spending[total_spending['Category'] != 'Income']
    print()
    print('This is the highest total spending with category')
    print(total_spending.loc[total_spending['Total_Spending'] == total_spending['Total_Spending'].max()])
    print()

def save_transaction_to_csv(df):
    print()
    csv_name = input("write down file name plz.: ")
    df.to_csv(f'{csv_name}.csv', index=False)
    print('complete')
    print()

def monthly_spending_trend(df):
    df[['Year','Month','Day']] = df['Date'].str.split('-', expand= True)
    spending = df[df['Category'] != 'Income']
    spending.groupby('Month')['Amount'].plot(kind='line')
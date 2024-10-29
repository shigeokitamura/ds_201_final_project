from datetime import datetime


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
    print(range_date)


def analyze_spending_by_category(df):
    total_spending = df.groupby('Category')['Amount'].sum()
    total_spending = total_spending.reset_index()
    total_spending.columns = ['Category', 'Total Spending']
    print(f'This is total spending for each category.')
    print(total_spending)

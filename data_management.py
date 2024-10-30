from datetime import datetime

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



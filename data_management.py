import pandas as pd
from datetime import datetime
import visualization

def del_transaction(df):
    print(df)
    while True:
        delete = input("Enter the index of the transaction to delete: ")
        delete = int(delete)
        index_data = list(df.index)
        if delete in index_data:
            df = df.drop(delete)
            print("Transaction deleted successfully!")
            break
        else:
            print("Invalid index")
            print("Please try again")
            print()
            continue
    return df

def add_transaction(df):
    # print(df)
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(f"'{datetime}' is not a valid format (YYYY-MM-DD)")
            print("Please try again")
            print()
            continue

        category = input("Enter the category (e.g., Food, Rent): ")
        category = category.capitalize()

        description = input("Enter a description: ")
        description = description.capitalize()

        amount = input("Enter the amount: ")
        if not amount.isnumeric():
            print(f"{amount} is not a valid format ")
            print("Please try again")
            print()
            continue
        ex_or_inc = input("Is it an Income or an Expense: ")
        ex_or_inc = ex_or_inc.capitalize()
        if ex_or_inc not in ["Income", "Expense"]:
            print(f"{ex_or_inc} is not a valid format")
            print("Please try again")
            print()
            continue

        data = {'Date': [date], 'Category': [category], 'Description': [description], 'Amount':[amount], 'Type': [ex_or_inc]}
        df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)

        print("Transaction added successfully!")
        print()
        break
    return df

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

    while True:
        user = input('Do you want to see pie chart representing the distribution of spending across categories? (Yes/No)')
        if user.lower() in ['yes','y']:
            visualization.distribution_of_spending_by_categories(df)
            print()
            break
        elif user.lower() in ['no', 'n']:
            print('Back to the menus')
            print()
            break
        else:
            print("Follow the format (Yes/No)")
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

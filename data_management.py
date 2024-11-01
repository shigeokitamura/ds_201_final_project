import pandas as pd
from datetime import datetime

def del_transaction(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return
    print()
    index = pd.Index(range(1,len(df)+1))
    df.index = index
    df = df.sort_values('Date')
    print(df.to_string(index=True))
    while True:
        delete = input("Enter the index of the transaction to delete (If you want to go back, just press 0): ")
        index_data = list(df.index)
        try:
            delete = int(delete)
        except ValueError:
            print('You should the number of index or 0: ')
            continue

        if int(delete) in index_data:
            df = df.drop(delete)
            print("Transaction deleted successfully!")
            print()
            break
        elif delete == 0:
            break
        else:
            print("Invalid index")
            print("Please try again")
            print()
            continue
    return df.sort_values('Date')


def add_transaction(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

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
        try:
            amount = float(amount)
        except ValueError:
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
    return df.sort_values('Date')


def view_all_trans(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return
    df = df.sort_values('Date')
    print()
    print('--- All Transactions ---')
    print(df.to_string(index=False))
    print()


def view_trans_by_date_range(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

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
    if len(range_date) == 0:
        print()
        print('No transactions found in this date range.')
        print()
        return
    range_date = range_date.sort_values('Date')

    print()
    print(f'--- Transactions from {start_date} to {end_date} ---')
    print(range_date)
    print()


def save_transaction_to_csv(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

    print()
    csv_name = input("write down file name plz.: ")
    df.sort_values('Date').to_csv(f'{csv_name}.csv', index=False)
    print('Complete')
    print()


def edit_transaction(df):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return
    df = df.sort_values('Date')
    print(df)
    while True:
        edt = input("Enter the index of the transaction to edit: ")
        edt = int(edt)
        index_data = list(df.index)

        if edt in index_data:
            print("Current Transaction Details:")
            print(df.loc[edt])

            new_date = input("Enter the date (YYYY-MM-DD) or press Enter to keep current: ")
            if new_date != "":
                try:
                    datetime.strptime(new_date, "%Y-%m-%d")
                except ValueError:
                    print(f"'{datetime}' is not a valid format (YYYY-MM-DD)")
                    print("Please try again")
                    print()
                    continue
            new_category = input("Enter new category or press Enter to keep current: ")
            new_category = new_category.capitalize()
            new_description = input("Enter new description or press Enter to keep current: ")
            new_description = new_description.capitalize()
            new_amount = input("Enter new amount or press Enter to keep current: ")
            if new_amount:
                try:
                    new_amount = float(new_amount)
                except ValueError:
                    print(f"{new_amount} is not a valid format ")
                    print("Please try again")
                    print()
                    continue
            else:
                new_amount = None
            new_type = input("Enter a new type(Income or Expense) or press Enter to keep current: ")
            new_type = new_type.capitalize()
            if new_type not in ["Income", "Expense", ""]:
                print(f"{new_type} is not a valid format")
                print("Please try again")
                print()
                continue

            if new_date != "":
                df.loc[edt, 'Date'] = new_date
            if new_category != "":
                df.loc[edt, 'Category'] = new_category
            if new_description != "":
                df.loc[edt, 'Description'] = new_description
            if new_amount is not None:
                df.loc[edt, 'Amount'] = new_amount
            if new_type != "":
                df.loc[edt, 'Type'] = new_type

            print("Transaction updated successfully!")
            print()
            break
        else:
            print("Invalid index")
            print("Please try again")
            print()
            continue
    return df.sort_values('Date')

def set_monthly_income(data: dict):
    while True:
        try:
            value = float(input("Enter your total monthly income: "))
            break
        except ValueError:
            print("Invalid income. Please enter again.")

    data["monthly_income"] = value
    print(f"Your monthly income is set to: ${value:.2f}")
    print()

    return data

def set_category_budget(df: pd.DataFrame, data: dict):
    if len(df) == 0:
        print()
        print('There is no file. Try again.')
        print()
        return

    categories = df[df["Type"] == "Expense"]["Category"].unique().tolist()
    budgets = {}

    while True:
        try:
            for category in categories:
                budget = float(input(f"Enter your budget for {category}: "))
                budgets[category] = budget
            break
        except ValueError:
            print("Invalid value. Please enter again")

    data["budgets"] = budgets

    print("Your budgets have been set:")
    for category in categories:
        print(f"- {category}: ${data['budgets'][category]:.2f}")
    print()

    return data

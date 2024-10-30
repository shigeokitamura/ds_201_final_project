import pandas as pd
from datetime import datetime

def add_transaction(df):
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
        df = pd.DataFrame(data)

        print("Transaction added successfully!")
        print()
        break
    return df

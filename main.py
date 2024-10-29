import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

import data_management
import budget_management
import data_analysis
import visualization


def import_a_csv_file() -> pd.DataFrame:
    data = pd.read_csv("sampledata.csv")
    return data

def view_all_trans(df):
    print(df)


def main():
    print("=== Personal Finance Tracker ===")
    while True:
        menus = [
            "Import a CSV File",
            "View All Transactions",
            "View Transactions by Date Range",
            "Add a Transaction",
            "Edit a Transaction",
            "Delete a Transaction",
            "Analyze Spending by Category",
            "Calculate Average Monthly Spending",
            "Show Top Spending Category",
            "Visualize Monthly Spending Trend",
            "Save Transactions to CSV",
            "Exit",
        ]

        for idx, menu in enumerate(menus):
            print(f"{idx}. {menu}")

        option = input("Choose an option (0-11): ")

        match option:
            case "0":
                df = import_a_csv_file()
            case "11":
                break
            case "1":
                try:
                    view_all_trans(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "2":
                try:
                    data_management.view_trans_by_date_range(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "6":
                try:
                    data_management.analyze_spending_by_category(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")

if __name__ == "__main__":
    main()

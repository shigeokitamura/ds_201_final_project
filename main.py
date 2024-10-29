import pandas as pd

import data_management
import budget_management
import data_analysis
import visualization


def import_a_csv_file() -> pd.DataFrame:
    data = pd.read_csv("sampledata.csv")
    return data


def main():
    print("=== Personal Finance Tracker ===")

    while True:
        menues = [
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

        for idx, menu in enumerate(menues):
            print(f"{idx}. {menu}")

        option = input("Choose an option (0-11): ")

        match option:
            case "0":
                df = import_a_csv_file()
            case "3":
                data_management.add_transaction()
            case "11":
                break


if __name__ == "__main__":
    main()

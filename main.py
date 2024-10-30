import pandas as pd
import data_management
import budget_management
import data_analysis
import visualization


def import_a_csv_file() -> pd.DataFrame:
    data = pd.read_csv("sampledata.csv")
    return data


def main():
    data = {}

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
            "Visualize Spending by Category",
            "Set Monthly Income",
            "Save Transactions to CSV",
            "Exit",
        ]

        for idx, menu in enumerate(menus):
            print(f"{idx}. {menu}")

        option = input(f"Choose an option (0-{len(menus)}): ")

        match option:
            case "0":
                df = import_a_csv_file()
            case "1":
                try:
                    data_management.view_all_trans(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "2":
                try:
                    data_management.view_trans_by_date_range(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "3":
                try:
                    df = data_management.add_transaction(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "5":
                try:
                    df = data_management.del_transaction(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "6":
                try:
                    data_management.analyze_spending_by_category(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "8":
                try:
                    data_management.top_spending_category(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "9":
                try:
                    visualization.monthly_spending_trend(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "10":
                try:
                    visualization.spending_by_category(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "11":
                data = data_management.set_monthly_income(data)
            case "12":
                try:
                    data_management.save_transaction_to_csv(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "13":
                break

if __name__ == "__main__":
    main()

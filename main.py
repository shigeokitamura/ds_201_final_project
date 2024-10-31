import pandas as pd
import data_management
import budget_management
import data_analysis
import visualization


def import_a_csv_file() -> pd.DataFrame:
    while True:
        print()
        user = input('Do you want to put your transaction? (Yes or No): ')
        if user.lower() in ['yes', 'y']:
            print()
            user_df = input('write down your csv file name. (filename.csv): ')
            try:
                data = pd.read_csv(user_df)
                print('create example csv file.')
                print('Complete')
                print()
                return data
            except FileNotFoundError:
                print('It is not in this folder. try again.')
            except Exception as e:
                print(f'An error occurred: {e}')
        elif user.lower() in ['no', 'n']:
            print('create example csv file.')
            print('Complete')
            print()
            data = pd.read_csv("sampledata.csv")
            return data
        else:
            print("Follow the format (Yes/No): ")


def main():
    print("=== Personal Finance Tracker ===")
    df = pd.DataFrame()
    data = {}
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

        option = input(f"Choose an option (0-{len(menus) - 1}): ")
        match option:
            case "0":
                df = import_a_csv_file()
            case "1":
                data_management.view_all_trans(df)
            case "2":
                data_management.view_trans_by_date_range(df)
            case "3":
                df = data_management.add_transaction(df)
            case "4":
                df = data_management.edit_transaction(df)
            case "5":
                df = data_management.del_transaction(df)
            case "6":
                data_analysis.analyze_spending_by_category(df)
            case "7":
                data_analysis.average_monthly_spending(df, data)
            case "8":
                data_analysis.top_spending_category(df)
            case "9":
                visualization.monthly_spending_trend(df)
            case "10":
                visualization.spending_by_category(df)
            case "11":
                data_management.set_monthly_income(data)
            case "12":
                data_management.save_transaction_to_csv(df)
            case "13":
                print()
                print('Exits the program:')
                print('Exiting the Personal Finance Tracker. Goodbye!')
                break


if __name__ == "__main__":
    main()

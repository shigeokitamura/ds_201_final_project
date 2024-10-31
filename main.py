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
            "Save Transactions to CSV",
            "Exit",
        ]

        for idx, menu in enumerate(menus):
            print(f"{idx}. {menu}")

        option = input("Choose an option (0-12): ")
        match option:
            case "0":
                df = import_a_csv_file()
            case "1":
                if len(df) != 0:
                    data_management.view_all_trans(df)
                else:
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
            case "4":
                try:
                    df = data_management.edit_transaction(df)
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
                try:
                    data_management.save_transaction_to_csv(df)
                except UnboundLocalError or ValueError:
                    print("There is no file.")
            case "12":
                break


if __name__ == "__main__":
    main()

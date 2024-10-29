import pandas as pd

def del_transaction(df):
    # data = pd.read_csv("sampledata.csv")
    print(df)
    while True:
        delete = input("Enter the index of the transaction to delete: ")
        delete = int(delete)
        index_data = list(df.index)
        if delete in index_data:
            data = df.drop(delete)
            print("Transaction deleted successfully!")
            break
        else:
            print("Invalid index")
            print("Please try again")
            print()
            continue
    print(df)
    return df

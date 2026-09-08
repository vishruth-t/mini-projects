import pandas as pd
from datetime import datetime
from datetime import date

df=pd.read_csv("ledger.csv", skiprows=1,names=['no','date','amount','category','account','type'])
# print(df)
account=pd.read_csv("accounts.csv")
print(account)
while True:
    choice=int(input("""Welcome to my expense tracker.
Choose any options below by the number:

0 - Exit
1 - Record expense
2 - Record Income
3 - Check Balance
4 - Check Transactions
5 - Add/Remove Account



"""))

    if choice == 0:
        break

    elif choice == 1:
        while True:
            temp=[]
            temp.append(len(df))
            datet=input("Enter the date in YYYY-MM-DD format(or 0 for current date): ")

            if datet=='0':
                temp.append(datetime.now().strftime('%Y-%m-%d'))
            else:
                try:
                    isvalid = datetime.strptime(datet, "%Y-%m-%d")
                    temp.append(datet)
                    print(f"date recorded {datet}")
                except ValueError: 
                    print("Invalid Value! Try again")
                    continue
            
            amountt=float(input("Enter the amount to debit: "))
            categoryt=input("Enter the category of expense(Shopping,food,etc.): ")
            accountt=input("Enter the account to debit it from: ")
            
            if accountt not in account.columns:
                print("Invalid account, try again!")
                continue
            temp.extend([amountt,categoryt,accountt,'Expense'])
            account.loc[0, accountt] -= amountt
            
            df.loc[len(df)] = temp
            print(df)
            df.to_csv("ledger.csv",index=False,header=False)
            account.to_csv("accounts.csv",index=False,header=True)
            break

    elif choice==2:
        while True:
            temp=[]
            temp.append(len(df))
            datet=input("Enter the date in YYYY-MM-DD format(or 0 for current date): ")

            if datet=='0':
                temp.append(datetime.now().strftime('%Y-%m-%d'))
            else:
                try:
                    isvalid = datetime.strptime(datet, "%Y-%m-%d")
                    temp.append(datet)
                    print(f"date recorded {datet}")
                except ValueError: 
                    print("Invalid Value! Try again")
                    continue
            
            amountt=float(input("Enter the amount to credit: "))
            categoryt=input("Enter the category of income(Salary, CM ,etc.): ")
            accountt=input("Enter the account to credit it to: ")
            
            if accountt not in account.columns:
                print("Invalid account, try again!")
                continue
            temp.extend([amountt,categoryt,accountt,'Income'])
            account.loc[0, accountt] += amountt
            
            df.loc[len(df)] = temp
            print(f"{df}\n \n")
            df.to_csv("ledger.csv",index=False,header=False)
            account.to_csv("accounts.csv",index=False,header=True)
            break
    
    elif choice==3:
        print("Available accounts")
        for i in account:
            print(f"{i} - {account.loc[0,i]}")
        print()
    
    elif choice==4:
        print("All transactions: ")
        print(df)
        for i in range(len(df)):
            print(f"{account.iloc[i,0]} | {account.iloc[i,1]} | {account.iloc[i,2]} | {account.iloc[i,3]} | {account.iloc[i,4]} | {account.iloc[i,5]}")


    elif choice==5:
        print("Current accounts: ")
        while True:
            for i in account:
                print(f"{i} - {account.loc[0,i]}")
            print()
            
            choice_a=input("Do you want to add(1), remove(2) or modify existing account(3)? or (0) to go back: ")
            if choice_a == '0':
                break

            elif choice_a == '1':
                acc_name=input("Enter the name of the account: ")

                if acc_name in account:
                    print("ERROR! Account already exists")
                    print("Try again?")
                    continue
                
                acc_bal=input("Enter the balance for this account: ")

                account[f"{acc_name}"]=acc_bal
                print(f"{acc_name} - {acc_bal}")
                choice_con=input("Confirm changes? (1) - Yes, (2) - No")
                if choice_con=='1':
                    account.to_csv("accounts.csv",index=False,header=True)
            elif choice_a == '2':
                acc_name=input("Enter the name of the account: ")

                if acc_name not in account:
                    print("ERROR! Account does not exist")
                    print("Try again?")
                    continue
                print(f"Are you sure to delete this account  {acc_name} - {account[acc_name]}")
                choice_con=input("(1) - Yes, (2) - No: ")

                account = account.drop(acc_name, axis=1)
                account.to_csv("accounts.csv",index=False,header=True)
                
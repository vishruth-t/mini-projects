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
4 - Add/Remove Account
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
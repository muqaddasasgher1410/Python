from abc import ABC , abstractmethod
import csv

# Class Account
class account:
    def __init__(self, owner, account_no, balance):
        self.owner = owner
        self.account_no = account_no
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Your current amount is:{amount}")
        
    @abstractmethod 
    def withdraw(self):
        pass
    def monthly_process(self):
        pass
    
    # Class SavingAccount
class SavingAccount(account):
    def __init__(self, owner, account_no, balance, interest_rate):
        super().__init__(owner, account_no, balance)
        self.interest_rate = interest_rate
    def withdraw(self, amount):
        self.blance = self.balance - amount
        return f"Your current amount is:{amount}"
    def monthly_process(self, amount):
       interest_rate =  self.balance * (interest_rate) /12
       return f"add: {interest_rate} Your new balance is: {self.balance}"
   
    # Current Amount
class CurrentAccount(account):
    def __init__(self, loan_limit, fees):
        self.loan_limit = loan_limit
        self.fees = fees
        
    # Class Bank
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    def add(self, Account: account):
        self.accounts[Account.account_no] = Account
    def get(self, account_no):
        return self.accounts[account_no]
    def transfer(self, account_no_from, account_no_to, amount):
        src = self.get(account_no_from)
        desti = self.get(account_no_to)
        src.withdraw(amount)
        desti.deposit(amount)
        
  #  CSV
    def load_from_csv(self):
        file = "Account.csv"
        with open(file, "r") as f:
            read = csv.DictReader(f)
            for row in read:
                account_type = row.get("account_type") or  ""
                account_owner = row.get("owner") or ""
                account_no = row.get("account_no") or ""
                account_balance = row.get("balance") or ""
                rate = row.get("interest_rate") or ""
                limit = row.get("loan_limit") or ""
                if account_type == "SavingAccount":
                    type = SavingAccount("Owner", "account_no", "balance")
                elif account_type == "CurrentAccount":
                    type = CurrentAccount("loan_limit", "balance", "fees")
                else:
                    raise ValueError("This type of account is not defined!")
                self.add(type)
              
                
    def Save_to_csv(self, file = "Account.csv"):
        with open(file, "w") as f:
            header = ["Account_type", "Account_owner", "Account_balance", "loan_limit", "fees"]
            writer = csv.writer(f)
            writer.writerow(header)
        for acc in self.accounts.values():
            writer.writerow("CurrentAccount" , "acc.owner", "acc.no", "acc.balance")
    print("File is saved")
    def show_acc(self, file = "Account.csv"):
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
    def show(self):
        for i in self:
            print(i)
    def options(self):
        print("Enter 1 to show Accounts:")
        print("Enter 2 to add Accounts:")
        print("Enter 3 to load Account_no:")
        print("Enter 4 to Exit:")
        
    num = input("Enter a number: ")
    if num == 1:
        bank.show()
    elif num == 2:
        bank.add(acc3)
    elif num == 3:
        bank.account_no()
    else:
        exit()
    
bank = Bank("Islamic bank")
acc3 = SavingAccount("Muqaddas", "S_618", 5000, 1000)
acc4 = CurrentAccount("Muqaddas", "S_1027", 50000, 5000)
bank.add(acc3)
bank.add(acc4)
acc3.deposit(10000)
bank.load_from_csv("Account.csv")
bank.Save_to_csv("Account.csv")
bank.options()
                
            

        
        
        
        
        
    
        
        
        
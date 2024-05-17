import uuid

class Account:
    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type =account_type
        self.balance=0
        self.loan_count=0
        self.transaction_history=[]
        self.account_no = str(uuid.uuid4())

    def deposit(self,amount):
        self.balance +=amount
        self.transaction_history.append(('Deposit',amount))

    def withdraw(self,amount):
        if amount > self.balance:
            return "withdrawal amount exceeded" 
        else:      
            self.balance-=amount
            self.transaction_history.append(('withdraw',amount))
    
    def check_balance(self):
        return self.balance
    
    def check_transaction_history(self):
        return self.transaction_history
    
    def take_loan(self,amount):
        if self.loan_count <2:
            self.balance +=amount
            self.loan_count +=1
            self.transaction_history.append(('Loan',amount))
        else:
            return"Loan limit exceeded"
        
    def transfer(self,amount,other_account):
        if amount >self.balance:
            return "Insufficient balance"
        else:
            self.balance-=amount
            other_account.balance+=amount
            self.transaction_history.append(('Transfer',amount,other_account.account_no))

    def  interact(self):
        while True:
            print("1.Deposit")
            print("2. withdraw")
            print("3. Check balance")
            print("4. check transaction history")
            print("5. take loan")
            print("6. Transfer")
            print("7.Exit")
            choice= input("Enter your choice:")
            if choice =='1':
                amount= float(input("Enter amount:"))
                self.deposit(amount)
            elif choice=='2':
                amount=float(input("Enter amount:"))
                print(self.withdraw(amount))
            elif choice=='3':
                print("Balance:",self.check_balance())
            elif choice=='4':
                print("Transaction history:",self.check_transaction_history())
            elif choice=='5':
                amount=float(input("Enter amount :"))
                print(self.take_loan(amount)) 
            elif choice=='6':
                amount= float(input("Enter amount :"))
                other_account_no=input("Enter other account number:")
                if other_account_no in bank.accounts:
                     other_account= bank.accounts[other_account_no]
                     print(self.transfer(amount,other_account))
                else:
                    print("Account does not exist")
            elif choice=='7':
                 break
            else:
                print("Invalid choice")


class Bank:
    def __init__(self):
        self.accounts={}
        self.total_balance=0
        self.total_loan=0
        self.loan_status=True

    def create_account(self,name,email,address,account_type):
        new_account = Account(name,email,address,account_type)
        self.accounts[new_account.account_no] = new_account
        
    def delete_account(self,account_no):
        if account_no in self.accounts:
            del self.accounts[account_no]
        
    def show_users(self):
        for account_no,account in self.accounts.items():
            print(f"Account NO: {account_no},Name:{account.name}")
    
    def total_balance(self):
        total =0
        for account in self.accounts.values():
            total +=account.balance
        return total
    
    def total_loan(self):
        total =0
        for account in self.accounts.values():
            total +=account.loan_count
        return total
    

    def interact(self): 
        while True:
            print("1. Create account")
            print("2. Delete account")
            print("3. Show users")
            print("4. Total balance")
            print("5. Total loan")
            print("6. Exit")
            choice= input("Enter your choice:")
            if choice =='1':
                name =input("Enter name:")
                email= input("Enter email: ")
                address =input("Enter address:")
                account_type= input("Enter account type:")
                self.create_account(name,email,address,account_type)
            elif choice=='2':
                account_no = input("Enter account number")
                self.delete_account(account_no)
            elif choice == '3':
                self.show_users()
            elif choice =='4':
                print("Total balance:",self.total_balance())
            elif choice=='5':
                print("Total loan :",self.total_loan())
            elif choice =='6':
                break
            else:
                print("Invalid Choice")   

bank=Bank()
bank.interact()

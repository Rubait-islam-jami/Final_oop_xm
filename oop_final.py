import uuid

class Account:
    def __init__(self,name,email,address,account_type,password,account_no):
        self.name=name
        self.email=email
        self.address=address
        self.account_type =account_type
        self.password = password 
        self.balance=0
        self.loan_count=0
        self.transaction_history=[]
        self.account_no = account_no

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
        if bank.loan_status:
            if self.loan_count <2:
              self.balance +=amount
              self.loan_count +=1
              bank.total_loan += amount
              self.transaction_history.append(('Loan',amount))
            else:
               return"Loan limit exceeded"
        else:
           return "Loan disabled"
    
        
    def transfer(self,amount,other_account):
        if amount >self.balance:
            return "Insufficient balance"
        else:
            self.balance-=amount
            other_account.balance+=amount
            self.transaction_history.append(('Transfer',amount,other_account.account_no))
class Bank:
    def __init__(self):
        self.accounts={}
        self.total_balance=0
        self.total_loan=0
        self.loan_status=True

    def create_account(self,name,email,address,account_type,password,account_no):
        new_account = Account(name,email,address,account_type,password,account_no)
        self.accounts[new_account.account_no] = new_account
        return account_no
    
    def delete_account(self,account_no):
        if account_no in self.accounts:
            del self.accounts[account_no]
        else:
            print("Account does not exist")
        
    def show_users(self):
        for account_no,account in self.accounts.items():
            print(f"Account NO: {account_no},Name:{account.name}")
    
    def total_balance(self):
        total =0
        for account in self.accounts.values():
            total +=account.balance
        return total
    
    def total_loan(self):
        return self.total_loan
    

    def admin_menu(self): 
        while True:
            print("\nAdmin Menu:")
            print("1. Create account")
            print("2. Delete account")
            print("3. Show users")
            print("4. Total balance")
            print("5. Total loan")
            print("6. Enable/Disable loans")
            print("7.logout")
            choice= input("Enter your choice:")
            if choice =='1':
                name =input("Enter name:")
                email= input("Enter email: ")
                address =input("Enter address:")
                account_type= input("Enter account type (user/admin):")
                password= input(" Enter password :")
                account_no= input("enter new account number :")
                if account_no in self.accounts:
                    print("Already exists")

                account_no = self.create_account(name,email,address,account_type,password)
                print(f"Account created successfully.Account no:{account_no}")

            elif choice=='2':
                account_no = input("Enter account number")
                self.delete_account(account_no)
            elif choice == '3':
                self.show_users()
            elif choice =='4':
                print("Total balance:",self.total_balance())
            elif choice=='5':
                print("Total loan :",self.total_loan_amount())
            elif choice =='6':
                self.loan_status = not self.loan_status
                status ="enabled" if self.loan_status else "disabled"
                print(f"Loan functionlity is now {status}")
            elif choice == '7':
                break
            else:
                print("Invalid Choice")   



    def  user_menu(self,user_account):
        while True:
            print("\nUser Menu:")
            print("1.Deposit")
            print("2. withdraw")
            print("3. Check balance")
            print("4. check transaction history")
            print("5. take loan")
            print("6. Transfer")
            print("7. Logout")
            choice= input("Enter your choice:")
            if choice =='1':
                amount= float(input("Enter amount:"))
                user_account.deposit(amount)
            elif choice=='2':
                amount=float(input("Enter amount:"))
                print(user_account.withdraw(amount))
            elif choice=='3':
                print("Balance:",user_account.check_balance())
            elif choice=='4':
                print("Transaction history:",user_account.check_transaction_history())
            elif choice=='5':
                amount=float(input("Enter amount :"))
                print(user_account.take_loan(amount)) 
            elif choice=='6':
                amount= float(input("Enter amount :"))
                other_account_no=input("Enter other account number:")
                if other_account_no in self.accounts:
                     other_account= self.accounts[other_account_no]
                     print(user_account.transfer(amount,other_account))
                else:
                    print("Account does not exist")
            elif choice=='7':
                 break
            else:
                print("Invalid choice")

    def login(self):
        account_no = input("Enter account number :")
        password = input("Enter password: ")


        if account_no in self.accounts:
           account=self.accounts[account_no]
           if account.password==password:
                if account.account_type == 'admin':
                   print("Admin logged IN")
                   self.admin_menu()
                else:
                   print(f"User {account.name} logged in successfully")
                   self.user_menu(account)
           else:
                print("Incorrect password")
        else:
           print("Account not found")

    def register(self):
        name =input("Enter name:")
        email= input("Enter email: ")
        address =input("Enter address:")
        account_type= input("Enter account type (user/admin):")
        password= input(" Enter password :")
        account_no= input("Enter A New Account No :")

        if account_no in self.accounts:
            print("Already exists") 

        account_no = self.create_account(name,email,address,account_type,password,account_no)
        print(f"Account created successfully.Account no:{account_no}")

    def interact(self):
        while True:
           print("\nWelcome to the Bank System")
           print("1. Login")
           print("2. Register")
           print("3. Exit")
           choice = input("Enter your choice: ")
           if choice == '1':
              self.login()
           elif choice =='2':
                self.register()
           elif choice == '3':
              break
           else:
             print("Invalid choice")

bank = Bank()
bank.interact()

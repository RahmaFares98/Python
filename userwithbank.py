import bank_account
#Create a file with the User class, including the __init__ 
class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {} # to store multiple accounts
#add account type and linked balance it with Bank_account 
    def add_account(self, account_name,initial_balance  ,int_rate=0.001):
        self.accounts[account_name] = bank_account.BankAccount(int_rate=int_rate, balance=initial_balance)
        return self
# make_deposit methods
    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"Error: Account '{account_name}' not found.")
        return self
#Add a make_withdrawal method to the User class
    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"Error: Account '{account_name}' not found.")
        return self
#Add a display_user_balance method to the User class
    def display_account(self, account_name):
        if account_name in self.accounts:
            print(f"{self.name}, for {account_name}, your balance is ${self.accounts[account_name].get_balance()}")
        else:
            print(f"Error: Account '{account_name}' not found.")
        return self
#Add a transfer_money method
    def transfer_money(self, account_name, recipient, recipient_account_name, amount):
        if account_name in self.accounts and recipient_account_name in recipient.accounts:
            if self.accounts[account_name].get_balance() >= amount:
                self.accounts[account_name].withdraw(amount)
                recipient.accounts[recipient_account_name].deposit(amount)
                print(f"Transfer of ${amount} from {account_name} to {recipient_account_name} successful.")
            else:
                print(f"Error: Insufficient funds for transfer from '{account_name}' to '{recipient_account_name}'")
        else:
            if account_name not in self.accounts:
                print(f"Error: Your account '{account_name}' not found.")
            if recipient_account_name not in recipient.accounts:
                print(f"Error: Recipient's account '{recipient_account_name}' not found.")
        return self
# Test code
account1= bank_account.BankAccount(int_rate=0.05, balance=15600).get_balance()
print(account1)
account2 = bank_account.BankAccount(int_rate=0.01, balance=2600).get_balance()
print(account2)
account3 = bank_account.BankAccount(int_rate=0.03, balance=7000).get_balance()
print(account3)
account4 = bank_account.BankAccount(int_rate=0.07, balance=600).get_balance()
print(account4)
# Create users and add accounts to them
user1 = User("Rahma")
user1.add_account("Savings", account1)  
user1.add_account("Checking", account3)  
user2 = User("Yaqin")
user2.add_account("Checking", account2)  
user2.add_account("Savings", account4)  

# Make deposits
user1.make_deposit("Savings", 200)
user1.make_deposit("Checking", 200)
user2.make_deposit("Savings", 400)
user2.make_deposit("Checking", 300)
# Make withdrawals
user2.make_withdrawal("Checking", 500)
user1.make_withdrawal("Checking", 500)

# Display balances
user1.display_account("Savings")
user1.display_account("Checking")
user2.display_account("Savings")
user2.display_account("Checking")

# Transfer money between users
user1.transfer_money("Savings", user2, "Checking", 100)
user2.transfer_money("Savings", user2, "Checking", 400)

# Display balances after transfer
user1.display_account("Savings")
user2.display_account("Checking")

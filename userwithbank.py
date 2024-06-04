class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # Dictionary to store multiple accounts
        
    def add_account(self, account_name, initial_balance):
        self.accounts[account_name] = BankAccount(initial_balance)
        return self
    
    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"Error: Account '{account_name}' not found.")
        return self
    
    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"Error: Account '{account_name}' not found.")
        return self
    
    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            print(f"{self.name}'s balance for account '{account_name}': ${self.accounts[account_name].balance}")
        else:
            print(f"Error: Account '{account_name}' not found.")
        return self

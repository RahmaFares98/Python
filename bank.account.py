class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

# Create 2 accounts
account1 = BankAccount(int_rate=0.02, balance=100)
account2 = BankAccount(int_rate=0.01, balance=200)

# First account: 3 deposits, 1 withdrawal, yield interest, display info
account1.deposit(50).deposit(100).deposit(25).withdraw(75).yield_interest().display_account_info()

# Second account: 2 deposits, 4 withdrawals, yield interest, display info
account2.deposit(150).deposit(200).withdraw(50).withdraw(75).withdraw(100).withdraw(25).yield_interest().display_account_info()

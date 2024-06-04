class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Insufficient funds for {self.name}")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_user.make_deposit(amount)
        else:
            print(f"Insufficient funds for transfer from {self.name}")
        return self

# Creating 3 instances of the User class
user1 = User("Guido van Rossum")
user2 = User("Monty Python")
user3 = User("Linus Torvalds")

# First user: 3 deposits and 1 withdrawal, then display balance
user1.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(100).display_user_balance()

# Second user: 2 deposits and 2 withdrawals, then display balance
user2.make_deposit(300).make_deposit(150).make_withdrawal(50).make_withdrawal(100).display_user_balance()

# Third user: 1 deposit and 3 withdrawals, then display balance
user3.make_deposit(500).make_withdrawal(100).make_withdrawal(50).make_withdrawal(200).display_user_balance()

# BONUS: First user transfers money to the third user and then print both users' balances
user1.transfer_money(user3, 50)
user1.display_user_balance()
user3.display_user_balance()

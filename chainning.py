class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"{self.name}'s balance: ${self.balance}")
        return self

# Example usage with chaining
guido = User("Guido")
guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

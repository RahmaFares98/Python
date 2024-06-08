#Create a BankAccount class with the attributes interest rate and balance
class BankAccount:
    def __init__(self,int_rate=0.01, balance=0):
            self.int_rate = int_rate
            self.balance = balance
#Add a deposit method to the BankAccount class
    def deposit(self, amount):
        self.balance += amount
        return self
#Add a withdraw method to the BankAccount class
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
#Add a display_account_info method to the BankAccount class
    def display_account(self):
        print(f"Balance: {self.balance}$")
        return self
#Add a yield_interest method to the BankAccount class  
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
#Create 2 accounts
account1 = BankAccount(int_rate=0.05, balance=1500)
account2 = BankAccount(int_rate=0.01, balance=200)
#the first account:make 3 deposits , 1 withdrawal,yield interest, display info
account1.deposit(200).deposit(600).withdraw(340).yield_interest().display_account()
# Second account: 2 deposits, 4 withdrawals, yield interest, display info
account2.deposit(1500).deposit(300).withdraw(450).withdraw(75).withdraw(100).withdraw(25).yield_interest().display_account()

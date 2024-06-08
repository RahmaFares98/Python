#Create a file with the User class, including the __init__ and make_deposit methods
class user:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def make_deposit(self, amount):
        self.amount=0;
        self.balance+=amount
        return self
#Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        if self.balance >= amount:
            self.balance-=amount
        else:
            print ("Can't Complete this process- No fund")
        return self
#Add a display_user_balance method to the User class
    def display_user(self):
        print(f"{self.name}, your balance equal= {self.balance}$")
        return self
#Add a transfer_money method
    def transfer_money(self,recipinet,amount):
        if self.balance>amount:
            self.balance-=amount
            recipinet.make_deposit(amount)
        else:
            print(f"Insufficient funds for transfer from{self.name }")
        return self
#Create 3 instances of the User class
Rahma=user("Rahma",300)
Basel=user("Basel",350)
Husam=user("Husam",1000)

# First user: 3 deposits and 1 withdrawal, then display balance
Rahma.make_deposit(200).make_deposit(700).make_deposit(1000).make_withdrawal(543).display_user()
# Second user: 2 deposits and 2 withdrawals, then display balance
Basel.make_deposit(300).make_deposit(230).make_withdrawal(300).make_withdrawal(300).display_user()
# Third user: 1 deposit and 3 withdrawals, then display balance
Husam.make_deposit(500).make_withdrawal(100).make_withdrawal(50).make_withdrawal(200).display_user()
#have the first user transfer money to the third user and then print both users' balances
Rahma.transfer_money(Husam ,500).display_user(),Husam.display_user()
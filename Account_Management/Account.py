class Bank_Account:
    def __init__(self, total_balance=100):
        self.total_balance= total_balance
    def total_balances(self):
        return  (f" Your current balance is: ${self.total_balance}")

    def deposit_balance(self,deposit):
                self.total_balance = self.total_balance + deposit
                print(f"your total balance now is: ${self.total_balance}")
      
    def withdraw_balance(self,withdraw):
        if self.total_balance < withdraw:
            print(f"${withdraw} cannot be withdrawn since balance is insufficient")

        elif self.total_balance > withdraw:
            self.total_balance = self.total_balance - withdraw
            print(f"${withdraw} has been withdrawn from your account")
            print(f"Total balance now is: ${self.total_balance}")
        else:
            pass

    
a= Bank_Account()
a.deposit_balance(500)
a.withdraw_balance(200)
a.total_balances()
a.deposit_balance(200)
a.total_balances()
a.withdraw_balance(500)
a.total_balances()
a.withdraw_balance(200)
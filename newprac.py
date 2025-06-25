class Account:
    def __init__(self,bal,accno):
        self.balance=bal
        self.accno=accno

accno1=Account(10000,240626)
print(accno1.balance)
print(accno1.accno)
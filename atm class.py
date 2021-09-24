class atm:
    def __init__(self):
        self.balance=0
        print("new account created")
    def deposit(self):
        amount=int(input("enter money"))
        self.balance=self.balance+amount
    def withdraw(self):
        amount=int(input("enter money u want to with draw"))
        if(amount>self.balance):
                   print("insufficient funds")
        elif(amount>=50000):
            print("no cash")
        else:
            self.balance=self.balance-amount
    def enquiry(self):
        print("your balance is ",self.balance)
        print("THANK YOU VISIT AGAIN")
a=atm()
a.deposit()
a.withdraw()
a.enquiry()
            

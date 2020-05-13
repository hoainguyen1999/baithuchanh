class Bank:
    account_type = "savings"
    location = "Guntur"
    def __init__(self, name, account_Number,balance):
        self.name = name
        self.balance=balance
        self.Account_type=Bank.account_type
        self.location=Bank.location

    def __repr__(self):
        print("welcome to the SBR ATM Machine")
        print("------------------------------")
        account_pin = int(input("Please enter your pin number"))
        if (account_pin==123):
               account(self)
        else:
               print("pin Incorrect. please try again")
               Error(self)
        return ' '.join([self.name,self.Account_Number])
    def Error(self):
        
        account_pin = int(input("Please enter your pin number"))
        if(account_pin==123):
            Account(self)
        else:
             print("Pin incorrect. Please try again")
             slef.Error()
    def account(self):
        print("your card number is:xxx xxx xxx 1337")
        print("would you like todeposit/withdraw/check salence?")
        print("""
     1)       balance
     2)       withdraw
     3)       deposit
     4)       quit
     """)
        option=int(input("please enter your choice:"))
        if(option==1):
            balance(self)
        elif(option==2):
            withdraw(self)
        elif(option==3):
            deposit(self)
        elif(option==4):
            exit()
    def balance(self):
        print("balance:",self.balance)
        account(self)
    def withdraw(self):
        w=int(input("please enter desired amount:"))
        if(self.balance>0 and self.balance>=w):
            self.balance=self.balance-w
            print("your transaction is successfull")
            print("your balance :",self.balance)
            print("")
        else:
            print("your transaction is canelled due to")
            print("amount is not sufficcient in your account")
        account(self)
    def deposit(self):
        d=int(input("please enter desired amount:"))
        self.balance=self.balance+d
        print("your transaction is successfull")
        print("your balance :",self.balance)
        account(self)
    def exit():
        print("exit")
t1 = Bank('mahesh', 1453210145,5000)

print(t1)
                   
pass
                           
        

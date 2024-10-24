import random
class Account:
    def __init__(self,name,email,address,acType):
        self.name=name
        self.email=email
        self.address=address
        self.acType=acType
        self.acNumber=random.randint(400,999)
        self.__balance=0
        self.transactionsHistory=[]
        self.loanTime=0
        self.loanAmount=0
        print(f"Congratulations! Account created successfully.\n Mr. {self.name} account no is {self.acNumber}. Please remember it or note down it.")
    def deposit(self,balance):
        self.__balance+=balance
        self.transactionsHistory.append(f"Deposit ==> {balance}")
    def withdrawl(self,balance):
        if self.__balance<balance:
            print(f"Withdrawal amount exceeded")
        else:
            self.__balance-=balance
            self.transactionsHistory.append(f"Withdraw ==> {balance}")

    def takeLoan(self,amount):
        if self.loanTime<2:
            self.loanTime+=1
            self.loanAmount+=amount
        else:
            print(f"You get already two loans")
    
    @property
    def availableBalance(self):
        return self.__balance
        # print(f"Available balance: {self.__balance}")
    
    @property
    def transactions(self):
        for i in self.transactionsHistory:
            print(f"{i}")

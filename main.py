class User:
    def __init__(self,name,email,address,acType):
        self.name=name
        self.email=email
        self.address=address
        self.acType=acType
        self.__balance=0
        self.transactionsHistory=[]
        self.loanTime=0
        self.loanAmount=0
    def deposit(self,balance):
        self.__balance+=balance
        self.transactionsHistory.append(f"Deposit ==> {balance}")
    def withdrawl(self,balance):
        if self.__balance<balance:
            print(f"Withdrawal amount exceeded")
        else:
            self.__balance-=balance
            self.transactionsHistory.append(f"Withdraw ==> {balance}")
            print(f"Withdrawal Successful.")

    def takeLoan(self,amount):
        if self.loanTime<2:
            self.loanTime+=1
            self.loanAmount+=amount
        else:
            print(f"You get already two loans")
    
    @property
    def availableBalance(self):
        print(f"Available balance: {self.__balance}")
    
    @property
    def transactions(self):
        for i in self.transactionsHistory:
            print(f"{i}")




ac1=User("User1","XYZ","XYZ","Savings")
ac1.availableBalance
ac1.deposit(1000)
ac1.withdrawl(500)
ac1.deposit(10000)
ac1.withdrawl(500)
ac1.transactions
ac1.availableBalance
ac1.takeLoan(500)
ac1.takeLoan(1000)

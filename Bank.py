from Account import Account
class Bank:
    def __init__(self):
        self.AccountList={}
        self.__totalBalance=0
        self.__totalLoanAmount=0
        self.__loanFeature=True
    def createAcc(self,name,email,address,acType):
        account=Account(name,email,address,acType)
        self.AccountList[account.acNumber]=account
    def deposit(self,x):
        self.__totalBalance+=x
    def withdraw(self,x):
        self.__totalBalance-=x
    def takeLoan(self,x):
        self.__totalLoanAmount+=x
    def loanStatus(self,x):
        self.__loanFeature=x    
    @property
    def totalBalance(self):
        print(f"Total Balance: {self.__totalBalance}")
    def accList(self):
        for key,value in self.AccountList.items():
            print(f"{value.name} {value.email} {value.address} {value.acType} {key}")


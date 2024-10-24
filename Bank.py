from Account import Account
class Bank:
    def __init__(self):
        self.__AccountList={}
        self.__totalBalance=0
        self.__totalLoanAmount=0
        self.__loanFeature=True
    def createAcc(self,name,email,address,acType):
        account=Account(name,email,address,acType)
        self.__AccountList[account.acNumber]=account
    def deposit(self,x):
        self.__totalBalance+=x
    def withdraw(self,x):
        self.__totalBalance-=x
    def takeLoan(self,x):
        self.__totalLoanAmount+=x
    def loanStatus(self,x):
        self.__loanFeature=x  
    @property 
    def checkLoanStatus(self):
        if self.__loanFeature==True:
           print(f"Loan Status of Bank: ON")
        else:
            print(f"Loan Status of Bank: OFF")
    @property
    def totalBalance(self):
        print(f"Total Balance: {self.__totalBalance}")
    @property
    def totalLoanAmount(self):
        print(f"Total loan amount: {self.__totalLoanAmount}")
    @property
    def accList(self):
        for key,value in self.__AccountList.items():
            print(f"{value.name} {value.email} {value.address} {value.acType} {key}")

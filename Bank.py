from Account import Account
class Bank:
    def __init__(self):
        self.__AccountList={}
        self.__totalBalance=0
        self.__totalLoanAmount=0
        self.__loanFeature=True
        self.__bankRuptcy=False
    
    @property
    def firstBankRuptcy(self):
        if self.__totalBalance<self.__totalLoanAmount:
                self.__bankRuptcy=True
        else:
            self.__bankRuptcy=False

    # create a user account
    def createAcc(self,name,email,address,acType):
        account=Account(name,email,address,acType)
        self.__AccountList[account.acNumber]=account

    # delete user account
    def deleteAc(self,accNo):
        if accNo in self.__AccountList:
           del self.__AccountList[accNo]
           print(f"{accNo} delete successfully.")
        else:
            print(f"Account {accNo} not found.")

    # update total bank balance
    def deposit(self,x):
        self.__totalBalance+=x

    # update total bank balance
    def withdrawal(self,x):
        self.__totalBalance-=x

    # checking loan status on off
    def isLoanPossible(self):
        return self.__loanFeature
    
    # total loan amount
    def takeLoan(self,x):
        self.__totalLoanAmount+=x

    # update total loan amount when any user deposit money
    def paidLoan(self,x):
        self.__totalLoanAmount-=x

    # update loan status
    def loanStatus(self,x):
        self.__loanFeature=x  

    # return user object
    def returnUser(self,accNo):
        if accNo in self.__AccountList:
            return self.__AccountList[accNo]
        

    # check account no is exist or not
    def checkAcNo(self,x):
        if x in self.__AccountList:
            return True
        else :
            return False
        
    # check account information for log in
    def checkAcInfo(self,acNo,name,email):
        if acNo in self.__AccountList:
            if self.__AccountList[acNo].name==name and self.__AccountList[acNo].email==email:
                print(f"Welcome, Mr. {name} !")
                return True
            else:
                print("You have entered wrong credential.")
                return False
            
    # change bankruptcy status
    def changeBankRuptcy(self,x):
        self.__bankRuptcy=x

    @property
    def checkBankRuptcy(self):
        if self.__bankRuptcy==True:
            return True
        else:
            return False

    @property
    def bankruptcyStatus(self):
        if self.checkBankRuptcy:
            print("Bankruptcy")
        else:
            print("Not Bankruptcy")   

    @property 
    def checkLoanStatus(self):
        if self.__loanFeature==True:
           print(f"Loan Status of Bank: ON")
        else:
            print(f"Loan Status of Bank: OFF")


    @property
    def availableBalance(self):
        return self.__totalBalance
        # print(f"Total Balance: {self.__totalBalance}")


    @property
    def totalLoanAmount(self):
        print(f"Total loan amount: {self.__totalLoanAmount}")


    @property
    def accList(self):
        for key,value in self.__AccountList.items():
            print(f"{value.name} {value.email} {value.address} {value.acType} {key}")


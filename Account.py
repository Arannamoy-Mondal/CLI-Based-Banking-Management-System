# from Bank import Bank
import random
class Account:
    def __init__(self,name,email,address,acType):
        self.__name=name
        self.__email=email
        self.__address=address
        self.__acType=acType
        self.__acNumber=random.randint(400,999)
        self.__balance=0
        self.__transactionsHistory=[]
        self.__loanTime=0
        self.__loanAmount=0
        print(f"Congratulations! Account created successfully.\n Mr. {self.__name} account no is {self.__acNumber}. Please remember it or note down it.")
    
    
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def address(self):
        return self.__address
    
    @property
    def acType(self):
        return self.__acType
    
    @property
    def acNumber(self):
        return self.__acNumber
    

    def deposit(self,balance,admin):
        if self.__loanAmount>0:
            if self.__loanAmount>balance:
                self.__loanAmount-=balance
                admin.paidLoan(balance)
                self.__transactionsHistory.append(f"Loan payment ==> {balance}")
                print(f"You loan amount paid {balance}. Due {self.__loanAmount}")
            else:
                balance-=self.__loanAmount
                self.__transactionsHistory.append(f"Loan payment ==> {self.__loanAmount}")
                print(f"You loan amount paid {self.__loanAmount}. Due 0")
                admin.paidLoan(self.__loanAmount)
                self.__loanAmount=0
                self.__balance+=balance
                admin.deposit(balance)
                self.__transactionsHistory.append(f"Deposit <== {balance}")
                print(f"Deposit {balance}")
        else:
         self.__balance+=balance
         admin.deposit(balance)
         self.__transactionsHistory.append(f"Deposit <== {balance}")


    def withdrawl(self,balance,admin):
        if self.__balance<balance or self.__balance<=self.totalLoanAmount:
            print(f"Withdrawal amount exceeded")
        else:
            self.__balance-=balance
            admin.withdrawal(balance)
            self.__transactionsHistory.append(f"Withdraw ==> {balance}")

    def takeLoan(self,amount):
        if self.__loanTime<2 or self.__balance>amount:
            self.__loanTime+=1
            self.__loanAmount+=amount
        elif self.__balance<=amount:
            print("Your loan amount and deposit balance is safe.")
        else:
            print(f"You get already two loans")
    
    @property
    def availableBalance(self):
        return self.__balance
        # print(f"Available balance: {self.__balance}")
    
    @property
    def transactions(self):
        for i in self.__transactionsHistory:
            print(f"{i}")

    @property
    def totalLoanAmount(self):
        return self.__loanAmount
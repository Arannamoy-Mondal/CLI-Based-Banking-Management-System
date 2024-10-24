from Bank import Bank
from Account import Account
admin=Bank()

def adminFeatures(option):
    if option==1:
        name=input("Enter account owner name:")
        email=input("Enter account owner email:")
        address=input("Enter account owner address:")
        accType=input("Enter account type (Savings/Current):")
        if accType.lower()=="savings" or accType.lower()=="current":
            admin.createAcc(name,email,address,accType)
        else:
            accType=input("Please correct account type. If you want to cancel the process enter E. OtherWise accountype")
            if accType.lower()=="savings" or accType.lower()=="current":
                admin.createAcc(name,email,address,accType)
            else:
                return
    elif option==2:
        pass
    elif option==3:
        admin.accList
    elif option==4:
        admin.totalBalance
    elif option==5:
        admin.totalLoanAmount
    elif option==6:
        admin.checkLoanStatus
        x=input("Loan feature (ON/OFF):")
        if x.lower()=="on":
            admin.loanStatus("True")
            admin.checkLoanStatus
        elif x.lower()=="off":
            admin.loanStatus("False")
            admin.checkLoanStatus
        else:
            print("Invalid option for loan status")



while True:
    userType=input("U for User, A for Admin, E for exit:")
    if userType.lower()=='a':
        while True:
            print("0 for exit.\n1 for creat an account.\n2 for delete user account.\n3 see all user accounts list.\n4 "+
              "total available balance of the bank.\n5 total loan amount.\n6 for on or off the loan feature of the bank.")
            option=input("Option:")
            if option=="0":
                break
            elif option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6":
               adminFeatures(int(option))
            else:
                print("Invalid input")
    elif userType.lower()=='u':
        print("Welcome to our bank")
    elif userType.lower()=='e':
        print("Thanks for visiting")
        break
    else:
        print("You have enter invalid option")
        

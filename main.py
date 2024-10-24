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
        admin.accList
        x=int(input("Enter account no:"))
        admin.deleteAc(x)
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


def userFeatures(option):
    if option==1:
        pass

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
        while True:
              print("Welcome to our bank.\n 1 for create account.\n2 for log in account.\e for log out.")
              option=input("Option:")
              if option=="1":
                  name=input("Enter your name:")
                  email=input("Enter your email:")
                  address=input("Enter your address:")
                  acType=input("Enter account type (Savings/Current):")
                  if acType.lower()=="savings" or acType.lower()=="current":
                      if acType.lower()=="savings":
                          acType="Savings"
                      else:
                          acType="Current"
                      print(name+email+address+acType)
                      admin.createAcc(name,email,address,acType)
                  else:
                      print("Incorrect account type.")
              elif option=="2":
                  pass
              elif option=="e":
                   break
              else:
                  print("Invalid input.")
        """
        agree=input("Do you have any account (Yes/No)?")
        if agree.lower()=="no":
            doYouWantCreateAc=input("Do you want to create account (Yes/No)?")
            if doYouWantCreateAc.lower()=="no":
                continue
            else:
                name=input("Enter your name:")
                email=input("Enter your email:")
                address=input("Enter your address:")
                acType=input("Enter account type (Savings / Current):")
                if acType.lower()=="savings" or acType.lower()=="current":
                    # Account(name,email,address,acType)
                    admin.createAcc(name,email,address,acType)
                else:
                    print("You have selected wrong account type. Please write correct type.")
                    continue
        while True:
            accNo=input("0 for exit, Otherwise enter account number:")
            logOut=False
            if logOut==True:
                print("Log Out Successful. Thanks for visiting.")
                break
            elif accNo=='0':
                break
            elif admin.checkAcNo(int(accNo))==True:
               print(f"Account verification successful.")
               name=input("Enter name:")
               email=input("Enter email:")
               acType=input("Account Type:")
               if admin.checkAcInfo(int(accNo),name)==True:
                   while True:
                       print("3 for deposit money.\n4 for check available balance.\n5 transactions history.\n6 get loan from"+
                             "the bank\n7 transfer money from your account to another account.\n0 for exit.")
                       option=input("Option:")
                       if option=="0":
                           print("Thanks for visiting")
                           logOut=True
                           break
            else:
                print("You have enter wrong credential.")"""

    elif userType.lower()=='e':
        print("Thanks for visiting")
        break
    else:
        print("You have enter invalid option")
        



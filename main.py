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
            if accType.lower()=="savings":
                accType="Savings"
            else:
                accType="Current"
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
        print(f"Total avialablebalance: {admin.availableBalance}")

    elif option==5:
        admin.totalLoanAmount
        # print(f"Total loan amount: {admin.totalLoanAmount}")

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

    elif option==7:
        admin.bankruptcyStatus
        x=input("Is the bank bankrupt(Yes/No)?")
        if x.lower()=="yes":
            admin.changeBankRuptcy(True)
        elif x.lower()=="no":
            admin.changeBankRuptcy(False)
        else:
            print("Invalid input")
        admin.bankruptcyStatus


def userFeatures(accNo,option):
    admin.firstBankRuptcy
    user=admin.returnUser(accNo)


    if option==2:  # deposit
        amount=int(input("Enter deposit amount:"))
        user.deposit(amount,admin,"self")
        # admin.deposit(amount)


    elif option==3: # Withdrawal 
        if admin.checkBankRuptcy==True:
            print("This bank is bankrupt")
            return
        amount=int(input("Enter withdraw amount:"))
        if user.availableBalance<amount:
            print("Withdrawal amount exceeded")
        elif admin.availableBalance<user.availableBalance or admin.availableBalance<amount:
            print("This bank is bankrupt")
        else:
            user.withdrawl(amount,admin)
            # admin.withdraw(amount)
            print(f"Withdrawal Successful.")


    elif option==4: # Available balance
        print(f"Available balance: {user.availableBalance}")


    elif option==5: # Transactions
        user.transactions


    elif option==6: # Take Loan
        if admin.checkBankRuptcy:
            print("This bank is bankrupt")
            return
        else:
            amount=int(input("Enter loan amount:"))
            if admin.availableBalance>amount:
               if admin.isLoanPossible()==True:
                   user.takeLoan(amount)
                   admin.takeLoan(amount)
               else:
                   print("Loan not possible.")
            else:
                print("This bank is bankrupt.")


    elif option==7:  # Transfer money
        if admin.checkBankRuptcy==True:
            print("This bank is bankrupt")
            return
        accNo1=int(input("Enter transfer money account no:"))
        if admin.checkAcNo(accNo1)==True and accNo!=accNo1:
            print(f"A/C: {accNo1} Found.")
            user2=admin.returnUser(accNo1)
            amount=int(input("Enter transfer amount:"))
            if amount>user.availableBalance:
                print("You have not enough balance.")
            else:
                user.withdrawl(amount,admin)
                user2.deposit(amount,admin,"self")
                print("Transfer successful.")
        else:
            print("Account does not exist")

    
    elif option==8: # Total loan amount
        print(f"Total Loan {user.totalLoanAmount}")
        

while True:
    userType=input("U for User, A for Admin, D for Deposit, E for exit:")
    if userType.lower()=='a':
        while True:
            print("0 for exit.\n1 for creat an account.\n2 for delete user account.\n3 see all user accounts list.\n4 "+
              "total available balance of the bank.\n5 total loan amount.\n6 for on or off the loan feature of the bank.\n"
              +"7 for the bankruptcy")
            option=input("Option:")
            if option=="0":
                break
            elif option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6" or option=="7":
               adminFeatures(int(option))
            else:
                print("Invalid input")
    elif userType.lower()=='u':
        while True:
              print("Welcome to our bank.\n1 for create account.\n2 for log in account.\n0 for exit.")
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
                    #   print(name+email+address+acType)
                      admin.createAcc(name,email,address,acType)
                  else:
                      print("Incorrect account type.")
              elif option=="2":
                  accNo=int(input("Enter account no:"))
                  flag=False
                  if flag==True:
                      print("Log out successful.")
                      break
                  if admin.checkAcNo(accNo)==False:
                      print("Account not found")
                  else:
                      print("Account identified")
                      name=input("Enter your name:")
                      email=input("Enter your email:")
                      if admin.checkAcInfo(accNo,name,email):
                          while True:
                               print("2 for deposit money.\n3 for withdrawl amount\n4 for check available balance.\n5 transactions history.\n6 get loan from"+
                             "the bank\n7 transfer money from your account to another account.\n8 for total loan amount.\n0 for log out.")
                               userOption=input("Option:")
                               if userOption=="0":
                                   print("Log Out Successful.")
                                   flag=True
                                   break
                               elif userOption=="8" or userOption=="2" or userOption=="3" or userOption=="4" or userOption=="5" or userOption=="6" or userOption=="7":
                                   userFeatures(accNo,int(userOption))
                               else:
                                   print("Invalid input")
                      else:
                          print("You have enter wrong credential.")
              elif option=="0":
                   break
              else:
                  print("Invalid input.")

    elif userType.lower()=='e':
        print("Thanks for visiting")
        break

    elif userType.lower()=="d":
        accNo=int(input("Enter account no:"))
        if admin.checkAcNo(accNo):
            print("Account found")
            name=input("Enter your name:")
            contact=input("Enter your contact no:")
            amount=int(input("Enter deposit amount:"))
            user=admin.returnUser(accNo)
            user.deposit(amount,admin,name+""+contact)
        else:
            print("Account not found")
    else:
        print("You have enter invalid option")
        



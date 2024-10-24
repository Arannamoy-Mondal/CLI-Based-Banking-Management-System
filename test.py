from Bank import Bank
from Account import Account

admin=Bank()
print(admin.checkBankRuptcy())
admin.changeBankRuptcy("True")
print(admin.checkBankRuptcy())
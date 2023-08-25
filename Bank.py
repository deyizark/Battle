import uuid
class Account():

    def __init__(self, account_number, account_holder, initial_balance):
        if initial_balance < 500.0:
            print("Ou dwe met 500 goud pou pi piti sou kont ou an ")
        else:
            self.account_number = account_number
            self.account_holder = account_holder
            self.initial_balance = initial_balance
        self.account_number = str(uuid.uuid4().int)[:8]
    def deposit(self, amount):
        self.amount = amount
        self.initial_balance += amount   
    def withdraw(self, amount):
        if amount > self.initial_balance:
            print("Kòb ou mete a twòp, ou pa gen tout sa !!!")
        else:
            self.amount = amount
            self.initial_balance -= amount
    def get_balance(self):
        print("Ou gen ",self.initial_balance,"goud sou kont ou")
    
    def __str__(self):
       return f"\nAccount Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.initial_balance} goud"
# Kreye yon kont
account1 = Account("003402", "Lub Lorry", 10000.00)

# Depo
account1.deposit(500.00)

# Retrè
account1.withdraw(200.00)

# Verifye balans
balance = account1.get_balance()

# Afiche enfòmasyon sou kont lan
print(account1)
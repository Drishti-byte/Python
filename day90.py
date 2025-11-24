#program to implement hierarchial inheritance
class BankAccount:
    def __init__(self, accno, name):
        self.accno = accno 
        self.name = name 
        
    def display(self):
        print("Account Number:", self.accno)
        print("Account Name:", self.name)
        
class SBI(BankAccount):
    def __init__(self, accno, name, amount, time, roi):
        print("------------------Details about SBI Bank--------------------")
        super().__init__(accno, name)
        self.amount = amount 
        self.time = time 
        self.roi = roi
        
    def display(self):
        super().display()
        print("Principal Amount:", self.amount)
        print("Rate of Interest:", self.roi)
        print("Time:", self.time)
        
    def deposit(self):
        interest = (amount * time * self.roi) / 100
        print("Interest credited:", interest)
        bal = amount + interest 
        print("Balance after interest:", bal)

class ICICI(BankAccount):
    def __init__(self, accno, name, amount, time, roi):
        print("------------------Details about ICICI Bank-------------------------")
        self.accno = accno 
        self.name = name 
        self.amount = amount 
        self.time = time 
        self.roi = roi 
    
    def display(self):
        print("Account Number:", self.accno)
        print("Name:", self.name)
        print("Principal Amount:", self.amount)
        print("Rate of Interest:", self.roi)
        print("Time:", self.time)
    
    def deposit(self):
        interest = (self.amount * self.time * self.roi) / 100
        print("Interest credited:", interest)
        bal = self.amount + interest 
        print("Balance after interest:", bal)    

accno = int(input("Enter your account number:"))
name = input("Enter your name:")
print("-"*40)
bank = BankAccount(accno, name)
bank.display()
print("-----------------Enter the details of your SBI bank Acc----------------------")
accno = int(input("Enter your account number:"))
name = input("Enter your name:")
amount = int(input("Enter the amount you want to deposit:"))
time = float(input("Enter the time period:"))
sbi = SBI(accno, name, amount, time, 7)
sbi.display()
sbi.deposit()
print("------------------Enter the details of your ICICI bank Acc-------------------")
accno = input("Enter your account number:")
name = input("Enter your name:")
amt = int(input("Enter the amount you want to deposit:"))
t = float(input("Enter the time period:"))
icici = ICICI(accno, name, amt, t, 10)
icici.display()
icici.deposit()
class account:
   def __init__(self,balance):
       if balance<0:
           self.balance=0.0
           print("initial bala was inavalid")
       else:
         self.balance=balance
   def credit(self,camt):
        if camt<=0:
            print("camt should not be negative")
            return False
        else:
            self.balance=self.balance+camt
            return  True
   def debit(self,damt):
       if damt>self.balance:
           print("debitted amount exceeded")
           return False
       else:
           self.balance=self.balance-damt
           return  True
   def getbalance(self):
       return self.balance
class savingsaccount(account):
    def __init__(self,balance,roi):
        super().__init__(balance)
        self.roi=roi
    def calculateIntrest(self):
        inter=(self.balance*1*self.roi)/100
        return inter
class checkingaccount(account):
    def __init__(self,balance,tf):
        super().__init__(balance)
        self.tf =tf
    def credit(self,camt):
        status=super().credit(camt)
        if status:
            self.balance=self.balance-self.tf
    def debit(self,damt):
        status=super().debit(damt)
        if status:
            self.balance=self.balance-self.tf
class currentaccount(account):
    def __init__(self,balance,od):
        super().__init__(balance)
        self.od=od
    def debit(self,damt):
        if self.balance>damt:
            self.balance=self.balance-damt
        else:
            tw=self.balance+self.od
            if tw>=damt:
                self.balance
ac1=account(10000.00)
ac1.credit(5000.00)
ac1.debit(7000.00)
print(ac1.getbalance())
ac2=account(-10000.00)
ac2.credit(5000.00)
ac2.debit(7000.00)
print(ac2.getbalance())
sal=savingsaccount(10000.00,12)
sal.credit(5000.00)
sal.debit(700.00)
print(sal.getbalance())
print(sal.calculateIntrest())
cal=checkingaccount(10000.00,25.00)
cal.credit(7000.00)
cal.debit(2000.00)
print(cal.getbalance())
cul=currentaccount(100000.00,25000.00)
cul.credit(75000.00)
print(cul.getbalance())
cul.debit(19000.00)
print(cul.getbalance())




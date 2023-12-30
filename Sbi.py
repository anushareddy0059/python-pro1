class Sbi:
   branch='palamaner'
   ifsc='sbi00026'
   manager='jagan'
   loc='chittor'
   def __init__(self,name,mob,acc,pan,balance):
     self.name=name
     self.mob=mob
     self.acc=acc
     self.pan=pan
     self.balance=balance
   
   def credit(self,amt):
    self.balance+=amt
   def debit(self,amt):                                                                                                                               
    self.balance-=amt
chandra=Sbi('nara chandra',987654321,123467890543,'CBNT098W',12)
lokesh=Sbi('nara lokesh',987654321,123467890543,'CBNT09687Y',15 )

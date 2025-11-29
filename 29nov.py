# abstraction  : 
"""
data privacy , data security 

1. class abstact ==> from abc import ABC ==> abstract base class   
2. func / method  ==> @abstractmethod
note :  abstract class can't be instantiated ,not creating object of  abstract class
"""
from abc import ABC,abstractmethod

"""class vehicle(ABC) :
    def start(self):
        pass 
    
class car(vehicle):
    def start(self): # 
        print("car start")

class motorcycle(vehicle):
    def start(self):
        print("motorcycle start")
        
c=car()
c.start()
m=motorcycle()
m.start()
"""

# abstract method :

class bank(ABC):
    def __init__(self,acname,branch):
        self.acname =acname
        self.branch =branch
    
    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass 

class SBI(bank):
    def __init__(self, acname, branch):
        super().__init__(acname, branch)
        self.__balance =25000 
        
    def deposit(self,amt):
        self.__balance +=amt
        print("SBI deposit amount is  :",amt)
    
    def withdraw(self,amt):
        self.__balance -=amt
        print("SBI withdraw amount is  :",amt)
        
    def get_balance(self):
        return self.__balance

    def set_balance(self,new_balance):
        self.__balance =new_balance
    
    def display(self):
        print("SBI acname is  :",self.acname)
        print("SBI branch is  :",self.branch)
        print("SBI balance is  :",self.get_balance())

s=SBI("ayaan","Thaltej")
print("SBI Balance before  deposit :",s.get_balance())
s.deposit(10000)
s.withdraw(18000)
print("SBI Balance after  deposit and withdraw :",s.get_balance())

print("update the SBI balance  using set method :")
s.set_balance(30000)
print("SBI Balance after update :",s.get_balance())
s.deposit(10000)
s.withdraw(18000)
print("SBI Balance after  deposit and withdraw :",s.get_balance())

"""
class hdfc(bank)  + int_rate  ==> 15000 int rate   30000 int rate ==> charges 
"""
   
        
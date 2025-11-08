# oop : 
"""
class  and  object : 

class :  blue  print  of  object 
object :  instance of class 

4  pillar : 

1 . inheritance  
2.  encapsulation  
3. polymorphism
4. abstaction  

"""
# class  and  object  : 
"""
class person :  # person  ==> class 
    def show(self):   # function  / method : self  keyword ==> member , method  access
        print("ayaan  class .")
p=person()   # p object  ==> person()
p.show()  # method  / function  

"""

# data member  :  public by default 

"""
class person :
    name ="ayaan"   # name age clg ==>  class data member 
    clg ="nirma"
    age =20

    # def show(self):
    #     print(self.name)
    #     print(self.age)
    #     print(self.clg)

p=person()
# p.show()
print(p.name)
print(p.age)
print(p.clg)
"""

# private class : private data member  accessible  only  within class .

"""
class person : 
    __name="ayaan"
    __age =20 
    __clg="Nirma"

    def  show(self):
        print("name :",self.__name)
        print("age :",self.__age)
        print("clg :",self.__clg)

p=person()
p.show()
"""
"""
print(p.__name)  # no accessible  outside the class .
print(p.__age)
print(p.__clg)
"""

# bank  : 

class bank:
    name="ayaan"
    age =20
    accno =7201901432
    balance =50000 

    def depsoit(self,amt):
        self.balance = self.balance +amt
        print("deposit  amt  successfully",amt)
        print("after deposit  balance is  : ",self.balance)
    
    def withdraw(self,amt):
        if self.balance -amt > 10000 :
            self.balance -=amt 
            print("withdraw amt  successfully",amt)
            print("after withdraw balance is  : ",self.balance)
        else :
            print("invalid  balance")
    
    def  check_balance(self):
        print("your final balance is  : ",self.balance)
    
b=bank()
# print(b.name)
# print(b.age)
# print(b.accno)
# print(b.balance)
accno=int(input("enter the accont  no  for verification  : "))
if accno ==b.accno:
# b.show()
    b.depsoit(10000)
    b.withdraw(5000)
    b.check_balance()
else :
    print("account  no is not verify plz try again.")
# accno : 

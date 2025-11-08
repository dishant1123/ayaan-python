# encapsualtion  : 
"""
data security ,single unit  

1.  get  method : data print
2 . set method  : new  value  set 
"""

"""class bank : 
    def __init__(self,name,accno,balance=0):
        self.__name =name   # private variable  ==> name  accno balance 
        self.__accno =accno
        self.__balance =balance
    
    def show(self):
        print("name is :",self.__name)
        print("accno is :",self.__accno)
        print("balance is :",self.__balance)
    
    def depsoit(self,amt):
        self.__balance = self.__balance +amt
        print("deposit  amt  successfully",amt)
        print("after deposit  balance is  : ",self.__balance)

    def withdraw(self,amt):
        self.__balance = self.__balance -amt
        print("withdraw amt  successfully",amt)
        print("after withdraw balance is  : ",self.__balance)
    
    def check_balance(self):
        print("your final balance is  : ",self.__balance)

b=bank("ayaan",7201901432,50000)
b.show()
b.depsoit(10000)
b.withdraw(5000)
b.check_balance()
"""        
# get method : 
"""
class bank :
    def __init__(self,name,accno,balance=0):
        self.__name =name   # private variable  ==> name  accno balance
        self.__accno =accno
        self.__balance =balance
    
    def get_name(self):
        return self.__name
 
    def get_accno(self):
        return self.__accno

    def get_balance(self):
        return self.__balance

b=bank("ayaan",7201901432,50000)
print(b.get_name())
print(b.get_accno())
print(b.get_balance())
"""

# set ,get : 

"""class bank :
    def __init__(self,name,accno,balance=0):
        self.__name =name   # private variable  ==> name  accno balance
        self.accno =accno
        self.__balance =balance
    
    def get_name(self):
        return self.__name
   
    def get_balance(self):
        return self.__balance

    def set_balance(self,new_balance):
        self.__balance =new_balance
        print("new balance is :",self.__balance)

    def depsoit(self,amt):
        self.__balance = self.__balance +amt
        print("deposit  amt  successfully",amt)
        print("after deposit  balance is  : ",self.__balance)

    def withdraw(self,amt):
        self.__balance = self.__balance -amt
        print("withdraw amt  successfully",amt)
        print("after withdraw balance is  : ",self.__balance)
    
    def get_balance(self):
        return self.__balance
    
b=bank("ayaan",7201901432,50000)
print("before using  set method : ")

b.depsoit(10000)
b.withdraw(5000)
print("your balance  is  :",b.get_balance())

print("after usiing set method : ")

b.set_balance(80000)
b.depsoit(10000)
b.withdraw(40000)
print("your balance  is  :",b.get_balance())
"""

# a="rishi"
# b=3

# print(a*a)

"""a="devam"
print("a",a)
"""

"""str1="save paper,save trees"
print(str1.find("ave",1))
"""
"""str1="Vishv,Aryan,Devarsh"
print(str1[6:11])
"""
# print("abcdef"[2:8])

# print('new'  'line')

"""x = ['ab', 'cd']
for i in x:
    i.upper()
print(i)
"""

"""x=['ab','cd']
for i in x :
    c =i.upper()
print(c)
"""

"""x = 'abcd'
for i in range (len(x)):
    i.upper()
print (x)
"""

"""str1 = "my isname isisis jameis isis bond"
str.count()
"""

"""str1 = "my isname isisis jameis isis bond"
sub = "is"
print(str1.count(sub))
"""
"""print("John" > "Jhon")
print("Emma" < "Emm")

t = [1, 2, 4, 3]
print(t)
"""

"""my_tuple = (1, 2, 3, 4,[5,6])
my_tuple[4].append("saloni")
print (my_tuple)
"""

"""a=(1,2,3,4)
del a
print(a)
"""

"""a=(0,1,2,3,4)
b=slice(1,3)
print(a[b])
"""

"""tupl=("annie","hena","sid")
print(tupl[-3:-1])
"""

tupl=([2,3],"abc",0,9)
#      0      1   2 3 
print(tupl[0][1])


# #  2,3 ==>0  ==> 2 ==>0 3 ==>1    1   2  3 
# tupl[0][1]=1  # ==> 2,3 
# print(tupl)

aTuple = ("Orange", (10, 20, 30), (5, 15, 25))


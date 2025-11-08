print("hello")


# data type  : 
"""
1. int  : pos or neg ==> no limit 
2. float :  decimal  value  ==> no limit 
3. complex num  : immginary  and real part   ex : 23 + 2j  23 real 2j  immiginary  
4. string  or char : a to z 
5. boolean :  true  false  ==> t=> 1 f=>0

"""
# user string  : 
"""a=input("enter the string  : ")
b =str(input("enter the surname  : "))
print(a)
print(b)
print(a,b)
print(a,end="")
print(b)
"""

# user num  : 

"""a=int(input("enter the num  : "))
b=float(input("enter the num  : "))
print(a)
print(b)
"""

# operator  : 
"""
1. airthematic : + / - * %  
2. comparison : < > <= >= == != 
3. logical  : and  ,or 
""" 
# conditional statement  : 
"""
if con :
    print
else :
    print
"""

"""
a=int(input("enter the num  : "))
b=int(input("enter the num  : "))

if a>b :
    print("a is big")
else :
    print("b is big")
"""
"""
x=("a is big") if a>b  else ("b is big" ) 
print(x)
"""

# ladder if  : 

"""
if  con : 
    print
elif con :
    print
else:
    print
"""

"""
a=int(input("enter the num  : "))
b=int(input("enter the num  : "))
c =int(input("enter the  num : "))

if  a>b and  a>c :
    print("a is big")
elif b>a and b>c:
    print("b is big")
else :
    print("c is big")

"""
# nested if  : 

"""
if con :
    if con :
        print
    else :
        print 
elif con :
    if con :
        print
    else :
        print
else 
"""

"""
a=int(input("enter the num  : "))
b=int(input("enter the num  : "))
c =int(input("enter the  num : "))

if a>b :   
    if a>c :
        print("a is big")
    else :
        print("c is big")
elif b>a :  
    if b>c :
        print("b is big")
    else :
        print("c is big")
"""

# task  : 1 convert  upper to lower and vice versa . 

"""
ch =input("enter the character :")

if (ch >='A' and  ch <='Z'):
    ch=chr(ord(ch)+32)
    print(ch)
else :
    ch=chr(ord(ch)-32)
    print(ch)
"""

# match  : 

a=int(input("enter the num  : "))
b=int(input("enter the num  : "))

print("welcome  my calculator")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.mod")

choice =int(input("enter the choice  : "))

match(choice):
    case 1 :
        print("sum : ",a+b)
    case 2 :
        print("sub : ",a-b)
    case 3 :
        print("mul : ",a*b)
    case 4 :
        print("div : ",a/b)
    case 5 :
        print("mod : ",a/b)


# loop :  for  while  while true 

"""
for  : 

for  variable  name  in range (start , end , step):
    print(variable name)

"""    
"""for i in range(1,101):
    print(i,end=" ")
""" 

"""
for i in range(100,-1,-1):  #start stop  step
    print(i,end=" ")
"""

"""
for i in range(1,100,3):  #start stop  step
    print(i,end=" ")
"""

# while  : 
"""
syntax : 

i= intial 
while con :
    print 
    inc/dec i+=1
"""
"""
i=1
while i<=100:
    print(i,end=" ")
    i+=2
"""
"""
i=100
while i>=1:
    print(i,end=" ")
    i-=2
"""

# while true  ==>  program  continue  == > exit  

"""
i=1 
while True:
    print(i,end=" ")
    i+=1
    if i==10:
        break
"""
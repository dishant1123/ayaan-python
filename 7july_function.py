#function  : 
"""
1. no arg  no return 
2. no arg  with return  
3. with arg no return  
4. with arg with return
"""
# no arg no return
"""def sum():
    a=10
    b=30
    c=a+b 
    print(c)
sum()
"""
# with arg no return
"""def sum(a,b):
    c=a+b
    print(c)
a=int(input())
b=int(input())
sum(a,b)
"""
# no arg  with return 

"""def sum():
    a=90
    b=89
    c=a+b
    return c 
print(sum())"""

# with arg with return
"""def sum(a,b):
    return a+b
print(sum(11,66))
"""
# *args : it only take a number  of arguments. 

"""def m(*args):
    return sum(args)
print(m(15,2,55,66,77,99,12,456,88))
"""

# **kwargs : 2 arg : ==>  only use in dict 

"""def d1(**kargs):
    for i , j  in kargs.items():
        print(f"{i}:{j}")
d1(name="ayyan",age=20,city="ahm")
"""

# local varibale  : within function access not outside  function  

"""def d2():
    x=199  # local varibale  
    print(x)
d2()"""
# print(x)  error  u can't access outiside the function 

# global varibale  :  access any where 

"""x =120   # global variable
def d2():
    print(x)
d2()
print(x)
"""
# global varibale modify using  global keyword:

x =120 
def d2():
    global x
    x =900
    print("after modify the x  value is  : ",x)
d2()
print(x)


"""
bank  application  : 
1. create account  : user name,  password  : 
2. login :  user name  password  match    login success :25000 
only sucessfull  ==> 25000  
3. deposit  : amount  :  add to balance :5000  bal =30000
4. withdraw : amount  :  deduct from balance  : 12000  bal =18000
5. check balance : display current balance   bal :18000
"""
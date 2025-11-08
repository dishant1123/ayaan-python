# lambda   : one liner function  
"""
syntax :

lambda args : expression

""" 
"""
def sum(a,b):
    return a +b
print(sum (1,2))
"""
"""x =lambda a,b : a+b
print(x(23,56))
"""

# if else : 

"""def big():
    a=10
    b=90
    if a>b :
        print("a is big")
    else :
        print("b is big")
big()"""

"""x =lambda a,b : print("a is  big")if a>b else  print("b is big")
x(12,89)
"""

# built in function  : len  min max  sorted sum 

"""
a= lambda x :  sorted(x)
print(a((12,2,3,4,5)))
"""

# filter  , map  : 

"""
filter  : information  filter ==> jan to dec fin trasc ==> june  

==> filter  ==> list no changes 
"""
# l1=[1,2,3,4,5,6,7,8,9,10]
"""even=[]
odd=[]
for i in l1 :
    if i %2==0:
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)

"""
"""
l1=[1,2,3,4,5,6,7,8,9,10]

a =list(filter(lambda x : x % 2==0,l1))
b =tuple(filter(lambda x : x % 2==1,l1))

print(a)
print(b)
"""

# map :  given  new  list : 
"""l1=[10,2,3,40,9,10]
a =list(map(lambda x :x *2 ,l1)) 
print(a)
"""

# sorted using lambda : 
l1 =[("science",100),("maths",29),("english",10),("physics",39),("history",49)]
# sci ,100   ==> 0  ==> sci ==>0  100==>1
# maths , 29 ==> 1  ==> maths ==>0  29==>1
# english , 10 ==> 2 ==> english ==>0  10==>1 
# physics , 39 ==> 3 ==> physics ==>0  39==>1
# history , 49 ==> 4 ==> history ==>0  49==>1

"""
a= sorted(l1,key=lambda x :x[0])
print(a)
"""

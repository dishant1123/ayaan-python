# tuple  : immutable sequence ==>  can't be changes in tuple  . 

"""
t1 =(1,2,3,4,5,6,"ayaan")
print(t1)
print(type(t1))

t2 =1,2,3,4,5,6,"ayaan"
print(t2)
print(type(t2))
"""

# built in function : len min max sorted sum  reversed

"""
t1 =(10,2,3,4,5,6,88,99,100)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))
print(sum(t1))
"""

# slicing  : 
"""
t1 =(10,2,3,4,5,6,88,99,100)

print(t1[2])
# t1[2] ="ayaan"   == >  error  bcz of tuple is immutable
# print(t1)

print(t1[:2])
print(t1[2:])
print(t1[2: 5 :2])
"""

# method : 

"""t1 =(10,2,3,4,5,6,88,99,100)

print(t1.index(4))
print(t1.count(100))
"""

#tuple unpacking

"""
t1 =(10,2,3,4,5,6,88,99,100)

a,b,c,d,e,f,g,h,i=t1 
#                 
print(a,b,c,d,e,f,g,h,i)
print(a)
print(b)
print(c)
"""
# convert : 
#task  : 1
"""
t1 =(10,2,3,4,5,6,88,99,100)
output = (10,2,3,4,5,6,88,99,100,"ayaan") 
"""

t1 =(10,2,3,4,5,6,88,99,100)
l2= list(t1) 
l2.append("ayaan")
print(tuple(l2))

# dict  :  mutable  ==>  changes in dict  ==>  key  , value  

"""
d1 ={"ayaan":20,"harsh" :21}
# ayaan  ==> key   20 value 
print(d1)
print(type(d1))

d2 ={20:"ayaan",45 :21}
print(d2)
print(type(d2))

"""
# dict  mutable : 

"""
d1 ={"ayaan":20,"harsh" :21}

d1["rishit"] =21
print(d1)
"""

# built in  function :  len min max sorted sum

"""
d1 ={"ayaan":20,"ashish" :21}

print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
"""
# print(sum(d1))

# method  : 

d1 ={"ayaan":20,"ashish" :21,"het":22}

"""d1.clear()
print(d1)
"""
"""d2=d1.copy()
print(d2)

print(d1.get("ashish"))

print(d1.keys())
print(d1.values())
print(d1.items())

"""
"""l1=["kavish","het"]

d2 =dict.fromkeys(l1,100)
print(d2)
"""
"""d1.pop("ayaan")
print(d1)
"""

"""
d1.popitem()
print(d1)
"""

# conversion  : 
"""d1={"ayaan":20,"ashish" :21,"het":22}

l1= list(d1)
print(l1)
print(tuple(d1))

s1 =str(d1)
print(s1)
print(type(s1))

"""
"""d1={}
for i in range(3):
    name =input("enter the name  : ")
    marks=int(input("enter the marks  : "))
    d1[name]=marks
print(d1)
# {'ayaan': 98, 'yash': 73, 'rishit': 58}  # d1.values() 98 73 58   
l1 =sorted(d1.values())  #   58 73 98 
d2={}

for i in l1 :  # 58 73 98 
    for  j, k  in d1.items():  #{'ayaan': 98, 'yash': 73, 'rishit': 58}
        if i == k :  # 58 == 58 
            d2[j]= i  # 
print(d2)
"""
"""
task  : 2 sort above dict asc order of marks :
output  : {'rishit': 58 'yash': 73, 'ayaan': 98}

task  : 3 
ask user to enter the string  and count  of the letter  and store in dict. 

input  : missisippi
output  : {'m': 1, 'p': 2, 's': 3, 'i': 4}
"""
s1 ="missisippi"

"""for i in s1 :
    if i in d1 :  
        d1[i]+=1  
        
    else : 
        d1[i]=1  
print(d1)
"""
# **kwargs :  use only in dict key  value  

def d1(**kwargs):
    print(kwargs.keys())
d1(a="saloni" ,b =20 , c ="jerry")



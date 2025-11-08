#string :  immutable  ==>  not changes in string  

"""
s1= "my name is ayaan  sheth."

print(s1)
print(type(s1))
"""
# built in  function :  len min max sorted 

"""
s1= "my name is ayaan sheth."
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
"""

# slicing  : 

"""
s1= "my name is ayaan sheth."
print(s1[0])
print(s1[2 : 5 ])
print(s1[  : 5 ])
print(s1[2  :  ])

print(s1[2  :10 : 2 ])
print(s1[: : -2])
print(s1[: : -1])
"""
"""
task  : 1 
s1 = ayaan sangin sheth 
output  : a.s.sheth

task  : 2 
ask user to enter the two string and interchange the  first three  letter . 

input  1 : color 
input  2 :full 

output1:fulor 
output2 :coll
"""
"""s1=input("enter the string  : ")
s2=input("enter the string  : ")

s3 =s1[0 :3] + s2[3 : ]
print(s3)
"""
# method : 

s1= "my name is Ayaan Ayaan Sheth."
"""print(s1.capitalize())
print(s1.lower())
print(s1.upper())
print(s1.swapcase())
print(s1.casefold())
print(s1.title())
"""
# print(s1.replace("Ayaan","yash",1))

"""
task  : 3 

input  : restart 
output : resta@t 

task  : 4 

input  :  my name is  ayaan sheth. 
output : my_name is ayaan_sheth.

"""

"""
s1= "restart" 
s2=s1[0]
# print(s2)
modify_string = s2 + s1[1 : ].replace(s2,"@")
print(modify_string)
"""

"""s1="my name is ayaan sheth." 

s2 = s1.replace(" ","_",1)[ : : -1].replace(" ","_",1)[ :: -1]
print(s2)
"""



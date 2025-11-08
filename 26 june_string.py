# s1="my name is ayaan sheth."
"""print(s1. split())
print(s1. split("a"))
print(s1. split("is"))

print(s1.rsplit("a"))
"""

"""print(s1.partition("is"))
print(s1.partition("a"))

print(s1.rpartition("a"))
"""
s1="my name is ayaan sheth."

"""print(s1.index("m"))
print(s1.index("ayaan"))
print(s1.index("a"))
print(s1.index("a",5 ,15))

print(s1.rindex("a"))  # r  ot  l  

print(s1.find("a"))
print(s1.find("ayaan"))
print(s1.find("a",5,15))

print(s1.rfind("a"))  # r  ot  l  
"""

# task  : 1 
"""
s1= i am going to goa next month.
output : first  o  index : 6 
second  o  index : 12
third   o  index : 15
fourth  o  index : 24

task  : 2 

input  :i love python languages. 

total  words : 4 
total  letter including space : 24 
logest word = languages

"""
"""s1 = "i love python languages."

s2 =s1.split()
s3 =""
# print("word count : ",len(s2))

# s3 = len(s1)
# print("total letter including space : ",s3)
for i in s2 :   # ["i" , "love" , "python" , "languages."]
    if len(i) > len(s3):
        s3=i
print("logest word = ",s3)
"""

# task  : 3
"""
input  : ["php", "maam", "python", "java"]
output : ['php', 'maam']

"""
"""l1 =["php", "maam", "python", "java"]
l2=[] 

for i in  l1:
    if i  == i[: : -1]:
        l2.append(i)
print(l2)
"""
"""
task : 2 
Write a Python program to count the number of strings from a given list of strings. 
	The string length is 2 or more and the first and last characters are the same.
	
	Sample List : ['abc', 'xyz', 'aba', '1221']
	Expected Result : ["aba" , "1221"]
"""
"""
task : 12 
Write a Python program to find strings in a given list containing a given substring.
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']

"""
"""l1 = [(('cat', 'dog', 'shatter', 'donut', 'at', 'todo',))]
l2=[]
for i in  l1 :  # cat 
    word = input("enter the word : ")  # ca 
    for  j in i :  # ca 
        if  word in  j :   #  ca   
            l2.append(j)
print(l2)"""

"""
take list from user append all element in list and print second  longest word in list  
         input : ["java", "python", "php","cpp","flutter"]
         output :  flutter"""
"""
l1= ["java", "python", "php","cpp","flutter"]
s2=""
for i in  l1 :  # php   
    if len(i) >  len(s2):  # 3  > 6  
        s2=i   #s2 = 6   
print(s2)
"""
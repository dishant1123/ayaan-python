#file  handling  : 
"""
txt file  : 

1. read mode : only exiting file  open  
2. write mode : new file  open + write + exiting  file  open  ==> overwrite 
3. append mode : new file  open + write + exiting  file  open  ==> append

with open () as f  

f.read()
f.write()
f.close()
"""
# w mode : 
"""
with open("ayyan.txt","w") as f :
    f.write("my name is ayaan\n")
    f.write("my age is 20\n")
    f.write("live in ahmedabad\n")
    f.close()
 
"""

#w mode exiting file  : 
"""with  open("ayyan.txt","w") as f :
    f.write("love cricket.\n")
    f.write("study in nirma university.\n")
    f.write("love to play cricket.\n")
    f.close()
"""

# a mode : 

"""
with open("ayyan_1.txt","a") as f :
    f.write("my name is ayaan\n")
    f.write("my age is 20\n")
    f.write("live in ahmedabad\n")
    f.write("love cricket.\n")
    f.close()
"""

# a mode exiting  file  : 
"""with open("ayyan_1.txt","a") as f :
    f.write("my best friend name is  yash.\n")
    f.write("food lover.\n")
    f.write("businees minded\n")
    f.close()
"""

# r mode : 
with  open("ayyan.txt","r") as f :
    # print(f.read())  # read all  lines 
    # print(f.readline())  # only first  line 
    print(f.readlines())   # all lines store in list 
    f.close()
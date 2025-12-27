# file handling  : 
"""
1.read  : only exiting  open  
2.write : new file create + write  + exiting  open ==> context ==> overwrite 
3.append: new file create + write  + exiting  open ==> context ==> last append  

function  : 
open ==> with  open  , fopen 
close ==> fclose 
read ==> read , readline  , readlines 
write ==> write , writelines
append ==> write 
"""

# w mode : 

"""
with  open("ayaan_shah.txt","w") as f :
    f.write("my name is ayaan shah.\n")
    f.write("live in ahmedabad.\n")
    f.writelines(["study in nirma university.\n","future goal is working in finance industry."])
    f.close()
"""
# w mode  exiting file  : 
"""
with  open("ayaan_shah.txt","w") as f :
    f.write("study in royal.\n")
    f.write("best friend name is yash parikh.\n")
    f.writelines(["live in ahemadabad.\n"])
    f.close()
"""

# a mode : 
"""
with  open("ayaan_shah12.txt","a") as f :
    f.write("my name is ayaan shah.\n")
    f.write("live in ahmedabad.\n")
    f.writelines(["study in nirma university.\n","future goal is working in finance industry."])
    f.close()
"""

# a mode exiting  file  : 
"""with  open("ayaan_shah12.txt","a") as f :
    f.write("best friend name is yash parikh.\n")
    f.write("setup business in india.\n")
    f.close()
"""

# read mode : 
"""
with  open("ayyan.txt") as f: 
    # context =f.read()  # read all file  context 
    # context = f.readline()  # only first  line 
    context= f.readlines()  # all lines print in list. 
    print(context)
    f.close()
"""
# task  :1 
"""
ask  user to enter the  number  store in to list and seprate odd and even  number to  odd.txt and even.txt. 

l1= [1,2,3,4,5]
odd.txt = [1,3,5]
even.txt = [2,4]
"""
"""l1= [1,2,3,4,5]
with open("odd.txt","w") as f: 
    for i in l1 :
        if i %2==1 :
            f.write(str(i) +"\n")
    f.close()
    
with open("even.txt","w") as f: 
    for i in l1 :
        if i %2==0 :
            f.write(str(i) +"\n")
    f.close()
            
"""

# task  :2
"""
ask  user to enter the  number  store in to list and seprate pellindrome in txt file. 

l1= [121,234,345,414,511]
peli.txt= 121 414 

r= num %10  
rev= rev *10 +r 
num = num //10 

if temp ==rev : 
"""
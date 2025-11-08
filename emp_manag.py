# emp  managment  system : 
"""
1. add 
2. delete 
3. update  
4. search  
5. display  

========================================================================
add + display : 
srno name   age  salary 
1    ayaan   20   1200000    
2    yash    21   15000

update  : 
enter srno   which  you want to update  : 1 
    name , age  , salary  :

serach  : 
enter srno  which you want to search : 1

delete  : 
enter srno  which you want to delete : 1

"""
d1={}
def add():
    id =int(input("enter the id: "))
    name =input("enter the name : ")
    age=int(input("enter the age "))
    salary=int(input("enter the salary "))
    d1[id] =[name,age,salary]
    print("added successfully")

def delete():
    id =int(input("enter the  id : "))
    if id in d1 :
        del d1[id]
    else :
        print("id not found")

def update():
    id=int(input("enter the id : "))
    if  id in d1 :
        age=int(input("enter the age : "))
        d1[id][1]=age
        print("updated successfully")
    else :
        print("id not found")

def search():
    id=int(input("enter the id : "))
    if id in d1 :
        print(d1[id])

    else :
        print("id not found")

def  display():
    for i in d1 :
        print(i,d1[i])
  
add()
add()
print("before update  : ")
print(d1)
delete()
print("after delete  : ")
print(d1)

display()
print(d1)

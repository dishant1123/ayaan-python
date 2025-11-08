# constrcutor : automatically called when object is  created. 
"""
1. default  constrcutor
2.parameterized  constrcutor
3. non-parameterized  constrcutor
4.constrcutor  over loading  

"""
# default  constructor
"""
class person : 
    def __init__(self):  # def  keyword , __init__ ==>  constrcutor / special method 
        print("hello ayaan")
        print("live in ahmedabad")

p=person()
"""
#non- parameterized  constructor

"""class person: 
    def __init__(self):
        self.name = "ayaan"
        self.age = 20
        self.clg = "nirma"

    def show(self):
        print("name is  :",self.name)
        print("age is :",self.age)
        print("cls is ",self.clg)
p=person()
p.show()
print(p.name)
print(p.age)
print(p.clg)
"""

# parameterized  constructor 

"""class person: 
    def __init__(self,name,age,clg):
        self.name =name 
        self.age =age
        self.clg=clg
    
    def show(self):
        print("name is  :",self.name)
        print("age is :",self.age)
        print("cls is ",self.clg)

p=person("ayaan",20,"nirma")
p.show()
"""

# construtor  over  loading  : 

class person : 
    def __init__(self):
        self.name ="ayaan"
        self.age =20
    
    def __init__(self):
        self.clg="nirma"
    
    def show(self):
        # print("name is  :",self.name)
        # print("age is :",self.age)
        print("cls is ",self.clg)

p=person()
p.show()

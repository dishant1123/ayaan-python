# inheritance : inheriting from base class property and method.

"""
1.single level inheritance
2.multiple level inheritance
3.multi level inheritance
4.hirearchy inheritance
5.hybrid inheritance
"""

# single level inheritance : 
"""
class a     == > base class 
 
class b(a)  ==> derived class
"""

#ex :1 
"""class student : 
    def display(self):
        print("student")

class teacher(student):
    def display(self):
        student.display(self)
        print("teacher")
        
t=teacher()
# t.show()
t.display()
"""

#ex :2 

"""class student : 
    def __init__(self):
        self.name ="ayaan"  # non parameterized constructor
        self.age =18 

class teacher(student):
    def __init__(self):
        super().__init__()   # base class constructor
        self.teacher_name = "prof. rav"
    def display(self):
        print("student name is  :",self.name)
        print("student age is  :",self.age)
        print("teacher name is  :",self.teacher_name)

t=teacher()
t.display()
t.name="yash"   # poss when data member is public . 
t.age=20
t.display()
"""

#ex :3 

"""
class emp : 
    def __init__(self):
        self.x =1
        
    def show(self):
        self.x=10 
        
class manager(emp):
    def __init__(self):
        super().__init__() 
    def show(self):
        self.x =self.x+1 
        print(self.x) 

m=manager()
m.show()       
"""
# option  a. 11   b.2   c.1   d none 

# 2. multiple inheritance  : 

"""
class a 

class b : 

class c(a,b):    # MRO  : ==> method resolution order
"""

class father :
    def __init__(self,f_name):
        self.f_name =f_name 

class mother :
    def __init__(self,m_name):
        self.m_name =m_name
        
class son(father,mother):
    def __init__(self,f_name,m_name,s_name):
        father.__init__(self,f_name)
        mother.__init__(self,m_name)
        self.s_name =s_name
    
    def display(self):
        print("son name is  :",self.s_name)
        print("father name is  :",self.f_name)
        print("mother name is  :",self.m_name)

s=son("sangin","labdhi","ayaan")
s.display()

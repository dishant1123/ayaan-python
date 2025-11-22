# multi level inheritance  : 
"""
class a :
class b(a) :
class c(b):
"""
"""class vehicle :
    def __init__(self,name,model):
        self.name  =name  
        self.model =model
        
    def display(self):
        print("vehicle name is  :",self.name)
        print("vehicle model is  :",self.model)

class car(vehicle):
    def __init__(self, name, model,speed):
        super().__init__(name, model)  # super () ==>called base class constructor 
        self.speed =speed 
    
    def display(self):
        vehicle.display(self) 
        print("car speed is  :",self.speed)
        

class motorcycle(car):
    def __init__(self, name, model, speed,seat):
        super().__init__(name, model, speed)  # super() ==> called base class constructor
        self.seat =seat 
        
    def display(self):
        vehicle.display(self) 
        print("motorcycle seat is  :",self.seat)
        print("motorcycle speed is  :",self.speed)

m=motorcycle("honda","V-123",200,3)
m.display()

c=car("BMW","X5",220)
c.display()
"""

# hybrid inheritance : two or more inheritance 

"""
class a :
class b(a) :

class c(a) :

class d(b,c)
"""

class employees :
    def __init__(self):
        self.name ="ayaan"
        self.age =18 
        

class manager(employees):
    def __init__(self):
        super().__init__()
        self.salary =90000 
        
class senior_manager(employees):
    def __init__(self):
        super().__init__()
        self.position ="senior manager of company"

class CEO(manager,senior_manager):# MRO  : METHOD RESOLUTION ORDER
    def __init__(self):
        manager.__init__(self)
        senior_manager.__init__(self)
        self.office ="new york"
    
    def display(self):
        print("CEO ofc is  :",self.office)
        print("manager salary is  :",self.salary)
        print("senior manager position is  :",self.position)
        print("employees name is  :",self.name)
        print("employees age is  :",self.age)

c=CEO()
c.display()

        
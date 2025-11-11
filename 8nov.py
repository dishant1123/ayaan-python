#encapsulation  : 
"""
data security ,single unit

1. get method  :  data print  
2. set method  :  new  value  set 
"""

class vehicle :
    def __init__(self,name,model):
        self.__name =name     # name  , model private   ==> function 
        self.__model =model
    
    # def get_name(self):
    #     return self.__name 
    
    # def get_model(self):
    #     return self.__model
    
    # def set_model(self,new_model):
    #     self.__model =new_model
    #     print("new model is :",self.__model)
        
v=vehicle("car","honda")
# print("vehicle name is  :",v.get_name())
# print("model is  :",v.get_model())

# print("using set method  : ")
# v.set_model("toyota")
# print("vehicle name is  :",v.get_name())
# print("model is  :",v.get_model())

"""
v.__model="toyota"  # not possible in private  only access  within class not  outside
print("model is  :",v.get_model())
"""

"""setattr(v,"model","toyota") 
setattr(v,"name","bike")
print(getattr(v,"model"))
print(getattr(v,"name"))
"""


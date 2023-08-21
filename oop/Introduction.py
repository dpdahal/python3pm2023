# # what is oop?
# # oop is a programming paradigm based on the concept of "objects", 
# #which can contain data, 
# #in the form of fields (often known as attributes or properties),
# # and code, in the form of procedures (often known as methods).

# # what is class?
# # A class is a blueprint for the object.

# # what is object?
# # An object is an instance of a class.

# # what is method?
# # A method is a function that is associated with an object.

# # what is attribute?
# # An attribute is a variable that is associated with an object.

# # what is self?
# # self represents the instance of the class.

# # class Introduction:
# #     x=10 

# #     def info(self):
# #         print("hello world")
    
# #     def add(self,a,b):
# #         print(a+b)

# # # instance of class
# # obj = Introduction()
# # print(obj.x)
# # obj.info()
# # obj.add(10,20)

# # what is constructor?
# # A constructor is a special type of method (function) 
# # which is used to initialize the instance members of the class.

# class Introduction:
#     # @staticmethod
#     # @classmethod
#     # @property
#     # setter and getter
#     # scope of variable
#     def __new__(self,*args,**kwargs):
#         print("hello new")
#         return super().__new__(self,*args,**kwargs)

#     def __init__(self):
#         print("hello constructor")

#     def info(self):
#         print("hello world")

#     def __str__(self):
#         return "hello str"


#     def __del__(self):
#         print("hello destructor")

    
# obj =Introduction()
# obj.info()


# class Mobile:
#     price =20000

#     def on(self):
#         print("mobile is on")

#     def off(self):
#         print("mobile is off")


# obj = Mobile()
# print(obj.price)
# obj.off()
# obj.on()

# a =5
# a=70
# print(a)  
  
class Human:
    __age=''

    def getAge(self):
        return self.__age
    
    def setAge(self,newage):
        self.__age = newage

obj = Human()
obj.setAge(50)
print(obj.getAge())

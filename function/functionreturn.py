# def A():
#     return [10,30]
    

# def B():
#     print(A())

# B()

# def take_value():
#      p = int(input("Enter the value of p: "))
#      t = int(input("Enter the value of t: "))
#      r = int(input("Enter the value of r: "))
#      return [p,t,r]

# def calculator():
#      data =take_value()
#      a = data[0]
#      b = data[1]
#      c = data[2]
#      return (a*b*c)/100
# def display():
#      print(calculator())

# display()

# def mul(num):
#     x =1
#     while x<=10:
#         print(num,"*",x,"=",num*x)
#         x+=1

# num = int(input("Enter the number: "))
# mul(num)
# def students():
#     data=['ram','sita','gita']
#     return data

# def add(new_name):
#     data = students()
#     data.append(new_name)
#     print(data)
   
# def display():
#     data = students()
#     for i in data:
#         print(i)

# # display()
# add('hari')
# a =40
# a+=50

# x=10
# def user():
#     global x
#     x=x+60
#     print(a)


# user()
# print(x)


# lambda function

# add = lambda x,y:x+y
# print(add(10,20))

# nested function 
# function decorator

# def add(x,y):
#     print(x+y)

# add(10,20)


# def A():
#     return 10


# def B():
#     print(A())

# B()


# def outer():
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#     inner()
# outer()

# def calculator():

#     def add(x,y):
#         return x+y
    
#     def sub(x,y):
#         return x-y
    
#     def mul(x,y):
#         return x*y
    
#     return [add,sub,mul]

# obj = calculator()
# print(obj[0](10,20))
# print(obj[1](10,20))
# print(obj[2](10,20))


# def total(x,y):
#     return x+y


# def sm(x,y,any_function):
#     print(any_function(x,y))

# x =int(input("Enter the value of a: "))
# y=int(input("Enter the value of b: "))
# sm(x,y,total)


# WAP to enter any number and check even or odd
# WAP to print the table of any number
# WAP to enter five subject marks and find the total and percentage


# def add(x,y):
#     return x+y


# print(add(10,20))


# what is decorator?
# decorator is a function which is used to
# modify the functionality of another function

# def outer_functio(any_function):
#     def inner_function(a,b):
#         if b==0:
#             return "B is zero"
#         else:
#             return any_function(a,b)
#     return inner_function


# @outer_functio
# def add(x,y):
#     return x+y

# print(add(10,0))
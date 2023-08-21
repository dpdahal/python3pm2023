# what is loop?
# loop is a repeating action until a condition is met
# there are two types of loop
# 1. for loop
# 2. while loop
# - nested loop

# what is for loop?
# for loop is a loop that use a
# variable to iterate through a list
# or a range of numbers
# or sequence of characters

# syntax
# for variable in list:
#   do something

# example

# users=['ram','shyam','hari','sita','gita']
# for name in users:
#     print(name)

# numbers=[1,2,3,4,5,6,7,8,9,10]
#
# for num in numbers:
#     if num%2==0:
#         print(num)


# data=['ram','sita','hari','krishna','gopal']
# for name in data:
#     if name=='ram' or name=='hari' or name=='gopal':
#         print(name)

# data=[
#     ['ram','sita','hari','krishna','gopal'],
#     ['laxmi','madan','diyan','bimal','sophia'],
# ]

# for y in data[0]:
#     print(y)

# for names in data:
#     for a in names:
#         print(a)

# for i in range(1,3):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")

# WAP to enter number of students and
# enter five subject marks of each student
# and calculate total and percentage and grad
# of each student

#
# num_of_student = int(input("Enter number of students: "))
# x=1
# total_marks=[]
# while x<=num_of_student:
#     print(f"=============Student: {x}================")
#     for mark in range(1):
#         nep = int(input("Enter nepali marks: "))
#         eng = int(input("Enter english marks: "))
#         math = int(input("Enter math marks: "))
#         sci = int(input("Enter science marks: "))
#         soc = int(input("Enter social marks: "))
#         total = nep+eng+math+sci+soc
#         total_marks.append(total)
#     x+=1
# for total in total_marks:
#     percentage = total/5
#     if percentage>=80:
#         print(f"Total: {total} Percentage: {percentage} Grade: A+")
#     elif percentage>=60:
#         print(f"Total: {total} Percentage: {percentage} Grade: A")
#     elif percentage>=50:
#         print(f"Total: {total} Percentage: {percentage} Grade: B")
#     elif percentage>=40:
#         print(f"Total: {total} Percentage: {percentage} Grade: C")
#     else:
#         print(f"Total: {total} Percentage: {percentage} Grade: D")

# users =['ram','sita','hari','ram','gita','hari']
# new_users=[]
# for name in users:
#     if name not in new_users:
#         new_users.append(name)
# print(new_users)
# users =set(users)
# for name in users:
# #     print(name)
# data=[
#     [12,34,54,45,56],
#     [34,56,67,78,89],
#     [23,45,56,67,78],
# ]
# x=0
# total=0
# while x<len(data):
#     a =0
#     while a<len(data[x]):
#         total+=data[x][a]
#         a+=1
#     x+=1
#
# print(total)


# studentsData = [
#     {'name': 'ram', 'gender': 'male', 'status': True},
#     {'name': 'hari', 'gender': 'male', 'status': False},
#     {'name': 'laxmi', 'gender': 'female', 'status': True},
#     {'name': 'sita', 'gender': 'female', 'status': False},
#     {'name': 'sophia', 'gender': 'female', 'status': False},
#     {'name': 'rita', 'gender': 'female', 'status': False},
# ]
# total_students = len(studentsData)
# total_male_students = 0
# total_female_students = 0
# total_active_male = 0
# total_inactive_male = 0
# total_active_female = 0
# total_inactive_female = 0
#
# for student in studentsData:
#     if student['gender'] == 'male':
#         total_male_students += 1
#     else:
#         total_female_students += 1
#
#     if student['status'] == True:
#         total_active_male += 1
#         total_active_female += 1
#
#     if student['status'] == False:
#         if student['gender'] == 'male':
#             total_inactive_male += 1
#         else:
#             total_inactive_female += 1
#
# print(f"Total Students: {total_students}")
# print(f"Total male: {total_male_students}")
# print(f"Total female: {total_female_students}")
# print(f"Total active male: {total_active_male}")
# print(f"Total active female: {total_active_female}")
# print(f"Total inactive female: {total_inactive_female}")
# print(f"Total inactive male: {total_inactive_male}")

#
# users = [
#     {'username': 'ram', 'password': 'ram123'},
#     {'username': 'sita', 'password': 'sita123'},
# ]
# username = input("Enter username: ")
# password = input("Enter password: ")
# login_success = False
# for user in users:
#     if user['username'] == username and user['password'] == password:
#         login_success = True
#
# if login_success:
#     print("Login success")
# else:
#     print("Username & password does not match")


# students = [
#     {'name': 'ram', 'email': 'ram@gmail.com', 'address': 'kathmandu'},
#     {'name': 'sita', 'email': 'sita@gmail.com', 'address': 'pokhara'},
#     {'name': 'hari', 'email': 'hari@gmail.com', 'address': 'biratnagar'},
#     {'name': 'gita', 'email': 'gita@gmail.com', 'address': 'kathmandu'},
# ]
#
# search = input("Enter name or email or address: ")
# status = False
# for student in students:
#     if student['name'] == search or student['address'] == search:
#         print(student)
#         status = True
#
# if status != True:
#     print("No data found")


# products = [
#     {'name': 'apple', 'price': 200, 'quantity': 10},
#     {'name': 'mango', 'price': 100, 'quantity': 20},
#     {'name': 'banana', 'price': 50, 'quantity': 30},
#     {'name': 'orange', 'price': 100, 'quantity': 40},
# ]
#
# for product in products:
#     product['total_price'] = product['price'] * product['quantity']
#     print(product)
#
# productsData = [
#     {
#         'category_name': 'Fruits',
#         'items': ['apple', 'mango', 'banana', 'orange'],
#     },
#     {
#         'category_name': 'Vegetables',
#         'items': ['potato', 'tomato', 'onion', 'cabbage']
#     },
#     {
#         'category_name': 'Grocery',
#         'items': ['rice', 'dal', 'salt']
#     }
# ]
#
# for product in productsData:
#     print(f"Category Name: {product['category_name']}")
#     print(f"Items: {product['items']}")
#     print(f'Total Items: {len(product["items"])}')
#     print("=====================================")

# numbers = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 56, 78],
#     [14, 15, 16, 17, 70]
# ]
# x=0
# total=0
# for num  in numbers:
#     if x==0:
#         for a in num:
#             total+=a
#     if x==len(numbers)-1:
#         total+=sum(num)
#     x+=1
# print(total)


# x = 0
# total = 0
# while x < len(numbers):
#     # first row
#     if x==0:
#         for a in numbers[x]:
#             total += a
#     # last row
#     if x==len(numbers)-1:
#         total +=sum(numbers[x])
#     x += 1
# print(total)


# numbers = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 56, 78],
#     [14, 15, 16, 17, 70]
# ]
#
# total = 0
#
# for x in numbers:
#     total+= x[0] + x[-1]
#
# print(total)

num = int(("Enter number of times: "))
x = 1
even_num = []
odd_num = []
while x <= num:
    n = int(input("Enter number: "))
    if n % 2 == 0:
        even_num.append(n)
    else:
        odd_num.append(n)
    x += 1

print(f"Even numbers: {even_num}")
print(f"Odd numbers: {odd_num}")

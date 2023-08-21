# handle = open('data.txt','w')
# handle.write('python')
# handle.close()

# handle = open('data.txt','a')
# handle.write('welcome \n')
# handle.close()

# obj = open('data.txt','r')
# print(obj.read())
#
# obj = open('users.txt','a')
# name = input('Enter your name: ')
# email = input('Enter your email: ')
# address = input('Enter your address: ')
# obj.write(name)
# obj.write("\n")
# obj.write(email)
# obj.write("\n")
# obj.write(address)
# obj.write("\n")
# obj.close()

nepali = int(input("Enter marks of Nepali: "))
english = int(input("Enter marks of English: "))
math = int(input("Enter marks of Math: "))
science = int(input("Enter marks of Science: "))
social = int(input("Enter marks of Social: "))
total = nepali + english + math + science + social
percentage = total / 5
division =''
if percentage >= 80:
    division = 'Distinction'
elif percentage >= 60:
    division = 'First'
elif percentage >= 45:
    division = 'Second'
else:
    division = 'Third'
obj = open('result.txt','a')
obj.write("Total: " + str(total))
obj.write("\n")
obj.write("Percentage: " + str(percentage))
obj.write("\n")
obj.write("Division: " + division)


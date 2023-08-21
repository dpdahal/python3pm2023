# print("============Computer Bazar=======")
# print("1. Dell(Rs: 20000 2. Toshiba(Rs:30000) 3. Mac(Rs: 50000)")
#
# option = int(input("Enter your option: "))
# if option == 1:
#     quantity = int(input("Enter the quantity: "))
#     dell_price = 20000*quantity
#     print("Total price: ", dell_price)
#
# elif option == 2:
#     quantity = int(input("Enter the quantity: "))
#     toshiba_price = 30000*quantity
#     print("Total price: ", toshiba_price)
# elif option == 3:
#     quantity = int(input("Enter the quantity: "))
#     mac_price = 50000*quantity
#     print("Total price: ", mac_price)
# else:
#     print("Invalid option")

age = int(input("Enter your age: "))
if age < 18:
    print("you are child")
elif age > 40:
    print("you are old")
else:
    print("Welcome to party")
    if age > 18 and age < 25:
        print("you drink only cocacola")
    else:
        print("you drink only beer")

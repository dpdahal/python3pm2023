# print("==========Nepal Yatayat  5km==========")
# print("1. Kalanki to Swayambhu")
# print("2. Kalanki to Baspark")
# print("3. Kalanki to Chabile")
# print("4. Kalanki to Koteshwor")
# print("5. Kalanki to Balkhu")
# print("6. Kalanki to kalanki")
#
# choice = int(input("Enter your choice: "))
# price=0
# if choice == 1:
#     question = input("Are you a student? (y/n): ")
#     if question == "y":
#         price = 15
#         price = price - (price * 0.1)
#         print("Your price is Rs.",price)
#     else:
#         price = 15
#         print("Your price is Rs.",price)
#
# elif choice == 2:
#     question = input("Are you a student? (y/n): ")
#     if question == "y":
#         price = 30
#         price = price - (price * 0.1)
#         print("Your price is Rs.",price)
#     else:
#         price = 30
#         print("Your price is Rs.",price)
#


print("1. ntc to ntc")
print("2. ntc to ncell")

choice = int(input("Enter your choice: "))
if choice==1:
    duration = int(input("Enter duration: "))
    if duration<=10:
        print("Your price is Rs. ",5)
    elif duration>10 and duration<=20:
        print("Your price is Rs. ",10)
    elif duration>20 and duration<=30:
        print("Your price is Rs. ",15)
    elif duration>30 and duration<=40:
        print("Your price is Rs. ",20)
    elif duration>40 and duration<=50:
        print("Your price is Rs. ",25)
    elif duration>50 and duration<=60:
        print("Your price is Rs. ",30)
    elif duration>60 and duration<=70:
        print("Your price is Rs. ",35)
    elif duration>70 and duration<=80:
        print("Your price is Rs. ",40)
    elif duration>80 and duration<=90:
        print("Your price is Rs. ",45)
    elif duration>90 and duration<=100:
        print("Your price is Rs. ",50)
    else:
        print("invalid duration")

# nep = float(input("Enter nepali marks: "))
# eng = float(input("Enter english marks: "))
# math = float(input("Enter math marks: "))
# sci = float(input("Enter science marks: "))
# comp = float(input("Enter computer marks: "))
# total = nep + eng + math + sci + comp
# per = total / 5
# print("Total marks: ", total)
# print("Percentage: ", per)

# users=[]
# name =input("Enter name: ")
# address =input("Enter address: ")
# city =input("Enter city: ")
# phone =input("Enter phone: ")

# users.append(name)
# users.append(address)
# users.append(city)
# users.append(phone)

# print(users)

users={
    "name":'ram',
    "address":[
        {'city':'ktm','phone':'123456789'},
    ],
    "contact":{
        "phone":'123456789',
        "email":'ram@gmail.com'
    }
}
print(users['address'][0]['phone'])
print(users['contact']['email'])
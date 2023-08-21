print("Capital of Nepal is: ")
print("1. Kathmandu")
print("2. Pokhara")
print("3. Biratnagar")
print("4. Birgunj")
correct_answer =[]
wrong_answer = []
option = int(input("Enter your answer: "))
if option == 1:
    print("Your answer is correct.")
    correct_answer.append(option)
else:
    print("Your answer is wrong.")
    wrong_answer.append(option)

print("Capital of India is: ")
print("1. Mumbai")
print("2. New Delhi")
print("3. Chennai")
print("4. Kolkata")

option2 = int(input("Enter your answer: "))
if option2 == 2:
    print("Your answer is correct.")
    correct_answer.append(option2)
else:
    print("Your answer is wrong.")
    wrong_answer.append(option2)
print(correct_answer)
print(wrong_answer)
percentage = len(correct_answer)/2*100
print("Your percentage is: ", percentage)
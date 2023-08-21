# what is regex?
# regex is a sequence of characters that define a search pattern

# ram123

import re

phone = 1234567898
# phone must be 10 digits
patterns = "^[0-9]{10}$"
if re.match(patterns, str(phone)):
    print("valid phone number")
else:
    print("invalid phone number")

# name ='ram thapa'
# name only contains alphabets and space
# patterns ="^[a-zA-Z\s]+$"

# patterns ="^([a-zA-Z]+)$"



# if re.match(patterns,name):
#     print("valid name")
# else:
#     print("invalid name")
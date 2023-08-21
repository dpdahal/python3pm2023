# what is function?
# function is a block of code which only runs when it is called.

# user define function
# def add(x,y):
#     return x+y
#
# print(add(5,6))
#
# def sub(x,y):
#     return x-y
#
# print(sub(5,6))

# import calendar
# print(calendar.calendar(2025))
# print(calendar.month(2021, 1))

# import datetime
#
# b_date = datetime.datetime(2023, 8, 15)
# today = datetime.datetime.now()
# if b_date > today:
#     print("your birthday is yet to come")
# else:
#     print("your birthday is gone")
# b_date = datetime.datetime(1998, 1, 1)
# today = datetime.datetime.now()
# print(today-b_date)
# print(datetime.datetime.now())

# pip install gTTS

from gtts import gTTS

import os
message = 'Happy Birthday to you'
language = 'en'
speech = gTTS(text=message, lang=language, slow=False)
speech.save("text.mp3")
os.system("start text.mp3")

# surajdm123@#$

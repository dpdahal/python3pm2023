import csv

with open('data.csv', 'r') as file:
    result = csv.reader(file)
    for a in result:
        print(a[2])

# a  =open('data.csv', 'r')
# print(a.read())
# a.close()
    
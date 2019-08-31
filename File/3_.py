""" WORK WITH JSON """
# http://docs.python.org/3/library/json.html

import json

"""Write Data JSON"""
# data = {}
# data['number'] = [
#     {"nama" : "Mutia", "skill" : "Program", "grade" : 90},
#     {"nama" : "Shafira", "skill" : "Coding", "grade" : 95,},
#     {"nama" : "Chairunisa", "skill" : "Gabut", "grade" : 80}
# ]

# with open('member.txt', 'w') as file:
#     json.dump(data, file)

"""Read Data JSON"""

with open('member.txt', 'r') as file:
    data = json.load(file)

    for x in data['number']:
        print(x)
        print("namanya adalah " + x["nama"] + " punya skill " + x["skill"] + " tingakatannya sudah " + str(x["grade"]))

# for x in range(0,2):
#     print("*****")
#
# a = int(input())
# for i in range(1,a):
#     for j in range(i,a):
#         print(" ")
#     for k in range(1,2*i-1):
#         print("*")
#     print()


# age=int(input("Enter you age: "))

# if(age<0):
#     raise ValueError("Age can not be Negative")

# if(age>18):
#     print("You can drive")
# else:
#     print("You can not drive")

# import math
# import math as m

# print(math.sqrt(36))
# print(math.cbrt(27))
# print(math.floor(2.89))
# print(math.ceil(2.89))
# print(math.factorial(5))

# radius=7
# print(math.pi*radius*radius)
# print(math.pi)
# print(m.pi)

import os

# print(os.getcwd())
# os.mkdir("Rohan")
# print(os.listdir())

# os.rename("Rohan","Shivam")
# os.remove("python.txt")
# os.remove("Shivam")

# os.rmdir("Shivam")
# for i in range(1000):
#     os.mkdir(f"Folder {i}")
# for i in range(1000):
#     os.rename(f"Folder {i}",f"MyFolder {i}")

# for i in range(1000):
#     os.rmdir(f"MyFolder {i}")

# Local Scope

num4=78

def sumProgram(num1,num2):
    num3=89
    print(num1+num2)
    # print(num3)
    print(num4)


sumProgram(4,7)
# print(num3)
# print(num4)
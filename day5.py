# a=7
# b=4
# print(a+b)

# a1=3
# b1=8
# print(a1+b1)

# def greet():
#     print("Hello Good Morning")

# def greet(str1):
#     print("Hello Good Morning",str1)

# def addTwoNum(num1,num2):
#     print("The sum is:",(num1+num2))


# greet()
# greet()
# greet()
# greet("Naitik")

# greet("Rohan")
# greet("kartik")

# addTwoNum(5,9)
# greet("Naitik")
# addTwoNum(2,4)
# greet("Neeraj")

# def mulTwoVal(num1,num2):
#     # print("Hello my name is khan")
#     return num1*num2
    
# print(mulTwoVal(4,5))
# print(mulTwoVal(2,3))


def square(side):
    area=side*side
    return area

def areaRect(l,b):
    area=l*b
    return area


# print(square(6))
# print(square(7))
# print("The area of Rectangle is: ",areaRect(7,5))

length=int(input("Enter the length: "))
breadth=int(input("Enter the breadth: "))

print("The area is: ",areaRect(length,breadth))
# a = {1, 2, 3}
# b = {2, 3, 4}

# if 2 in a:
#     print("Present")
# else:
#     print("Absent")

import turtle

window=turtle.Screen()
window.bgcolor("cyan")
window.title("SimpleGame")


myturtle=turtle.Turtle()
myturtle.color("blue")
myturtle.speed(1)

# for i in range(8):
#     myturtle.forward(100)
#     myturtle.right(90)

myturtle.goto(-100, 0)
myturtle.write("Hello World!", font=("Arial", 12, "bold"), align="left")

window.exitonclick()
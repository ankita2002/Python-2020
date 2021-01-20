from turtle import *

speed(1)
bgcolor("black")
color("red")
pensize(5)
for i in range(8):
    left(45)
    for i in range(8):
        forward(100)
        right(45)

hideturtle()

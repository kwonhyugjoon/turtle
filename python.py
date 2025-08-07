import turtle
import random

for i in range(1,3+1):
    turtle.penup()
    turtle.goto(random.randint(-300,300),random.randint(-300,300))
    turtle.pendown()
    turtle.circle(random.randint(10,100))

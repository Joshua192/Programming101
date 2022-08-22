from turtle import Turtle
from random import randint

james = Turtle()
james.color("red")
james.shape("turtle")

chris = Turtle()
chris.color("green")
chris.shape("turtle")

laura = Turtle()
laura.color("blue")
laura.shape("turtle")

def autoracer(x,y):
    x.penup()
    x.goto(-160,100+y)
    x.pendown()
    for i in range(0,150):
        x.forward(randint(0,5))


autoracer(james, 0)
autoracer(laura, 15)
autoracer(chris, 30)

from turtle import *

wn = getscreen

i = True

turtle = Turtle("turtle")
turtle.pensize(5)


def move(speed):
    player_input = input("")
    turtle.speed(speed)
    if player_input == ("w"):
        turtle.forward(20)
    elif player_input == ("d"):
        turtle.right(90)
        turtle.forward(20)
    elif player_input == ("s"):
        turtle.right(180)
        turtle.forward(20)
    elif player_input == ("a"):
        turtle.left(90)
        turtle.forward(20)


while i == True:
    move(1)

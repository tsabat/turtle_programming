from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape

screen = Screen()

# substitute 'subsample' for 'zoom' if you want to go smaller:
larger = PhotoImage(file="a.gif").subsample(3, 3)

screen.addshape(name="larger", shape=Shape("image", larger))

tortoise = Turtle("larger")

tortoise.stamp()

tortoise.hideturtle()

screen.exitonclick()

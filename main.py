from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape

screen = Screen()

# substitute 'subsample' for 'zoom' if you want to go smaller:
char_image = PhotoImage(file="char.gif").subsample(3, 3)
screen.addshape(name="char_shape", shape=Shape("image", char_image))

portal_image = PhotoImage(file="portal.gif")
screen.addshape(name="portal_shape", shape=Shape("image", portal_image))

char_turtle = Turtle()
char_turtle.shape("char_shape")

portal_turtle = Turtle()
portal_turtle.shape("portal_shape")

screen.exitonclick()

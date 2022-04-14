from turtle import *
from random import randrange
import os

turtle_pos1 = randrange(-200, 200)
turtle_pos2 = randrange(-200, 200)

wn = getscreen

t = Turtle("turtle")

while True:
    t.setpos(turtle_pos1, turtle_pos2)
    coordinates = (turtle_pos1, turtle_pos2)
    print(coordinates)

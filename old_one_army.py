from random import randrange
import turtle
import time
import os
from tkinter import PhotoImage

player_life = 300
counter = 0

wn = turtle.getscreen()
wn.title("old ones army")
wn.bgcolor("black")
portal_shape = os.path.expanduser("~/Desktop/portal.gif")
wn.addshape(portal_shape)


shape = PhotoImage(file="char.gif").subsample(3, 3)
wn.addshape(name="char", shape=shape)

player = turtle.Turtle("char")
player.color("black")
player.frame = 0


def portal_set_up(portal_shape):
    portal = turtle.Turtle()
    portal.shape(portal_shape)
    portal.color("black")
    portal.frame = 0
    return portal


counter = 0


def player_animate(counter):
    counter += 1

    if counter % 2 == 0:
        counter = 0
        player.shape("circle")
    else:
        player.shape("square")

    # print(player.shape)
    # if player.shape == "square":
    #     player.shape("circle")
    # elif player.shape() == "circle":
    #     player.shape("square")

    # player.shape("circle")

    wn.ontimer(player_animate, 500)


portal1 = portal_set_up(portal_shape)
portal2 = portal_set_up(portal_shape)

turtle.penup()

portal1.goto(-400, 0)
portal2.goto(400, 0)

while True:
    wn.update()

from turtle import *
from random import randrange

rock_pos1 = randrange(1, 200)
rock_pos2 = randrange(1, 100)
tager_pos1 = 0
tager_pos2 = 0


i = True

tt = getscreen()


def make_rock_new(count):
    coordintates = []
    counter = 0
    grid_size = 400
    while counter < count:
        p1 = randrange(-grid_size, grid_size)
        p2 = randrange(-grid_size, grid_size)
        rock = Turtle("square")
        rock.color("gray")
        rock.setpos(p1, p2)
        coordintates.append((p1, p2))
        counter += 1

    return coordintates


tager = Turtle("turtle")
tager.pencolor("red")
tager.pensize(5)

player = Turtle("turtle")
player.pencolor("blue")
player.pensize(5)

coordinates = make_rock_new(16)
print(coordinates)
# make_rocks(1)
# make_rocks(2)
# make_rocks(3)
# make_rocks(4)


def move(speed):
    player.speed(speed)
    player_move = input("")
    # if player_move == ("w"):
    #     player.forward(20)
    # else:
    #     if player_move == ("d"):
    #         player.right(90)
    #         player.forward(20)
    #     else:
    #         if player_move == ("s"):
    #             player.right(180)
    #             player.forward(20)
    #            else:
    #                if player_move == ("a"):
    #                    player.left(90)
    #                    player.forward(20)

    if player_move == "w":
        player.forward(20)
    elif player_move == "d":
        player.right(90)
        player.forward(20)
    elif player_move == "s":
        player.right(180)
        player.forward(20)
    elif player_move == "a":
        player.left(90)
        player.forward(20)

    pos = player.position()
    print(player.position())
    print(coordinates)
    if pos in coordinates:
        print("found")


def tager_move(speed):
    tager.speed(speed)
    tager_input = input("")
    # if player_move == ("w"):
    #     player.forward(20)
    # else:
    #     if player_move == ("d"):
    #         player.right(90)
    #         player.forward(20)
    #     else:
    #         if player_move == ("s"):
    #             player.right(180)
    #             player.forward(20)
    #            else:
    #                if player_move == ("a"):
    #                    player.left(90)
    #                    player.forward(20)

    if tager_input == "w":
        tager.forward(25)
    elif tager_input == "d":
        tager.right(90)
        tager.forward(25)
    elif tager_input == "s":
        tager.right(180)
        tager.forward(25)
    elif tager_input == "a":
        tager.left(90)
        tager.forward(25)


tager.pendown
tager.forward(100)
tager_pos1 += 100
tager.right(90)
tager.forward(100)
tager_pos2 -= 100
tager.left(90)
tager.penup


# print(tager_pos1, tager_pos2)


while i == True:
    print("player move")
    move(1)
    print("tager move")
    tager_move(1)

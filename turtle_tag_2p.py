from turtle import *
from random import randrange

rock_pos1 = randrange(1, 200)
rock_pos2 = randrange(1, 100)
tager_pos1 = 0
tager_pos2 = 0


i = True

tt = getscreen()


def make_rocks(level):
    if level == 1:
        rock_pos1 = randrange(-200, 200)
        rock_pos2 = randrange(-200, 200)
        rock_coordinates1 = (rock_pos1, rock_pos2)
        rock = Turtle("square")
        rock.color("gray")
        rock.setpos(rock_pos1, rock_pos2)
        rock_pos1 = randrange(-200, 100)
        rock_pos2 = randrange(-100, 200)
        rock_coordinates2 = (rock_pos1, rock_pos2)
        rock2 = Turtle("square")
        rock2.color("gray")
        rock2.setpos(rock_pos1, rock_pos2)
        rock_pos1 = randrange(-200, 200)
        rock_pos2 = randrange(-200, 300)
        rock_coordinates3 = (rock_pos1, rock_pos2)
        rock3 = Turtle("square")
        rock3.color("gray")
        rock3.setpos(rock_pos1, rock_pos2)
    elif level == 2:
        rock_pos1 = randrange(-200, 200)
        rock_pos2 = randrange(-200, 200)
        rock_coordinates4 = (rock_pos1, rock_pos2)
        rock = Turtle("square")
        rock.color("gray")
        rock.setpos(rock_pos1, rock_pos2)
        rock_pos1 = randrange(-200, 100)
        rock_pos2 = randrange(-100, 200)
        rock_coordinates5 = (rock_pos1, rock_pos2)
        rock2 = Turtle("square")
        rock2.color("gray")
        rock2.setpos(rock_pos1, rock_pos2)
        rock_pos1 = randrange(-200, 200)
        rock_pos2 = randrange(-200, 300)
        rock_coordinates6 = (rock_pos1, rock_pos2)
        rock3 = Turtle("square")
        rock3.color("gray")
        rock3.setpos(rock_pos1, rock_pos2)
    elif level == 3:
        rock_pos1 = randrange(-200, 200)
        rock_pos2 = randrange(-200, 200)
        rock_coordinates7 = (rock_pos1, rock_pos2)
        rock = Turtle("square")
        rock.color("gray")
        rock.setpos(rock_pos1, rock_pos2)
        rock_pos1 = randrange(-200, 100)
        rock_pos2 = randrange(-100, 200)
        rock_coordinates8 = (rock_pos1, rock_pos2)
        rock2 = Turtle("square")
        rock2.color("gray")
        rock2.setpos(rock_pos1, rock_pos2)
        rock_pos1 = randrange(-200, 200)
        rock_pos2 = randrange(-200, 300)
        rock_coordinates9 = (rock_pos1, rock_pos2)
        rock3 = Turtle("square")
        rock3.color("gray")
        rock3.setpos(rock_pos1, rock_pos2)
    elif level == 4:
        rock_pos1 = randrange(-200, 200)
        rock_pos2 = randrange(-200, 200)
        rock_coordinates10 = (rock_pos1, rock_pos2)
        rock = Turtle("square")
        rock.color("gray")
        rock.setpos(rock_pos1, rock_pos2)
        rock_pos1 = randrange(-200, 100)
        rock_pos2 = randrange(-100, 200)
        rock_coordinates11 = (rock_pos1, rock_pos2)
        rock2 = Turtle("square")
        rock2.color("gray")
        rock2.setpos(rock_pos1, rock_pos2)
        rock_pos1 = randrange(-200, 200)
        rock_pos2 = randrange(-200, 300)
        rock_coordinates12 = (rock_pos1, rock_pos2)
        rock3 = Turtle("square")
        rock3.color("gray")
        rock3.setpos(rock_pos1, rock_pos2)
    print(rock_coordinates1)
    print(rock_coordinates2)
    print(rock_coordinates3)
    print(rock_coordinates4)
    print(rock_coordinates5)
    print(rock_coordinates6)
    print(rock_coordinates7)
    print(rock_coordinates8)
    print(rock_coordinates9)
    print(rock_coordinates10)
    print(rock_coordinates11)
    print(rock_coordinates12)


tager = Turtle("turtle")
tager.pencolor("red")
tager.pensize(5)

player = Turtle("turtle")
player.pencolor("blue")
player.pensize(5)

make_rocks(1)
make_rocks(2)
make_rocks(3)
make_rocks(4)


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


tager.penup
tager.forward(100)
tager_pos1 += 100
tager.right(90)
tager.forward(100)
tager_pos2 -= 100
tager.left(90)
tager.pendown


print(tager_pos1, tager_pos2)


while i == True:
    move(1)
    tager_move(1)


tt.exitonclick()

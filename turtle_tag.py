from turtle import *

i = True

tt = getscreen()

player = Turtle("turtle")
player.pencolor("blue")
player.pensize(5)

turtle_tager = Turtle("turtle")
turtle_tager.pencolor("red")
turtle_tager.pensize(5)
turtle_tager.setpos(400, 50)


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


while i == True:
    move(4)


tt.exitonclick()

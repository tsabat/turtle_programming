from turtle import *

i = True

tt = getscreen()

player = Turtle("turtle")
player.pencolor("blue")
player.pensize(10)


def move(speed):
    player.speed(speed)
    player_move = input("")
    if player_move == ("w"):
        player.forward(20)
    else:
        if player_move == ("d"):
            player.right(90)
            player.forward(20)
        else:
            if player_move == ("s"):
                player.right(180)
                player.forward(20)
            else:
                if player_move == ("a"):
                    player.left(90)
                    player.forward(20)


while i == True:
    move(1)


tt.exitonclick()

from turtle import *
from pynput import keyboard

i = True

tt = getscreen()

player = Turtle("turtle")
player.pencolor("blue")
player.pensize(5)


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


print("Press s or n to continue:")

while i == True:
    # with keyboard.Events() as events:
    #     print("hi")
    #     # Block for as much as possible
    #     event = events.get(1e6)
    # print(event.key)
    # if event.key == keyboard.KeyCode.from_char("s"):
    #     print("YES")
    move(1)


tt.exitonclick()

from http.cookiejar import CookiePolicy
from re import I
from turtle import Turtle, Screen
import turtle

from random import randrange

SCREEN_X = 500
SCREEN_Y = 500

screen = Screen()
screen.setup(
    SCREEN_X,
    SCREEN_Y,
)
screen.setworldcoordinates(-SCREEN_X, -SCREEN_Y, SCREEN_Y, SCREEN_Y)
screen.bgcolor("dark salmon")


##screen.screensize(100, 100)


class Player(Turtle):
    BOX_SIZE = 5

    @property
    def _x(self):
        return self.position()[0]

    @property
    def _y(self):
        return self.position()[1]

    def pos(self):
        return (round(self._x), round(self._y))

    def is_hit(self, rocks):
        for rock in rocks:
            if is_in_box(
                (self._x - self.BOX_SIZE, self._y - self.BOX_SIZE),
                (self._x + self.BOX_SIZE, self._y + self.BOX_SIZE),
                rock,
            ):
                print(self.pos())
                print("Eaten")


player1 = Player()
player1.speed = 1

player1.shape("turtle")
player1.color("turquoise")
player1.penup()


def turn_left():
    player1.color("light green")
    player1.left(10)


def turn_right():
    player1.color("light green")
    player1.right(10)


def make_rocks(count):
    coordintates = []
    counter = 0
    grid_size = SCREEN_X

    while counter < count:
        p1 = randrange(-grid_size, grid_size)
        p2 = randrange(-grid_size, grid_size)
        rock = Player("square")
        rock.color("gray")
        rock.setpos(p1, p2)
        coordintates.append((p1, p2))
        counter += 1

    return coordintates


def is_in_box(bottom_left, top_right, point):
    if (
        point[0] > bottom_left[0]
        and point[0] < top_right[0]
        and point[1] > bottom_left[1]
        and point[1] < top_right[1]
    ):
        return True
    else:
        return False


coordinates = make_rocks(5)
# coordinates = [(3, 0)]
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")


screen.listen()

while True:
    player1.forward(1)

    # print(f"pos: {player.pos()}")
    # print(f"coordinates: {coordinates}")

    player1.is_hit(coordinates)

    # if player.pos() in coordinates:
    #     print("eaten!")

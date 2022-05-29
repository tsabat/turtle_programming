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
    def setup(self, color="green", speed=2):
        self.color = color
        self.speed = speed

    BOX_SIZE = 5

    @property
    def _x(self):
        return self.position()[0]

    @property
    def _y(self):
        return self.position()[1]

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def pos(self):
        return (round(self._x), round(self._y))

    def hit_check(self, rocks):
        for rock in rocks:
            if self._is_in_box(
                (self._x - self.BOX_SIZE, self._y - self.BOX_SIZE),
                (self._x + self.BOX_SIZE, self._y + self.BOX_SIZE),
                rock,
            ):
                print(self.pos())
                print("Eaten")

    def _is_in_box(self, bottom_left, top_right, point):
        if (
            point[0] > bottom_left[0]
            and point[0] < top_right[0]
            and point[1] > bottom_left[1]
            and point[1] < top_right[1]
        ):
            return True
        else:
            return False


def make_rocks(count):
    coordintates = []
    counter = 0
    grid_size = SCREEN_X

    while counter < count:
        p1 = randrange(-grid_size, grid_size)
        p2 = randrange(-grid_size, grid_size)
        rock = Turtle("square")
        rock.color("gray")
        rock.setpos(p1, p2)
        coordintates.append((p1, p2))
        counter += 1

    return coordintates


player1 = Player()
player1.setup()

player2 = Player()
player2.setup()


coordinates = make_rocks(5)
screen.onkeypress(player1.turn_left, "Left")
screen.onkeypress(player1.turn_right, "Right")
screen.onkeypress(player2.turn_left, "a")
screen.onkeypress(player2.turn_right, "d")

screen.listen()

while True:
    player1.forward(1)
    player2.forward(1)

    player1.hit_check(coordinates)
    player2.hit_check(coordinates)

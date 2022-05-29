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
    def setup(self, color="green", speed=5, rocks=5):
        self.color_name = color
        self.color(self.color_name)
        self.speed(speed)
        self.make_rocks(rocks)

    BOX_SIZE = 5

    def set_opponent(self, opponent: Turtle):
        self.opponent = opponent

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

    def rock_check(self):
        rock: Turtle
        for count, rock in enumerate(self.rocks):
            if self._is_in_box(
                (self._x - self.BOX_SIZE, self._y - self.BOX_SIZE),
                (self._x + self.BOX_SIZE, self._y + self.BOX_SIZE),
                rock,
            ):
                rock.hideturtle()
                self.rocks.remove(rock)
                if len(self.rocks) == 0:
                    print("no more rocks!")
                print(count)
                print(self.pos())
                print("Eaten")

    def _is_in_box(self, bottom_left, top_right, point: Turtle):
        point = point.pos()
        if (
            point[0] > bottom_left[0]
            and point[0] < top_right[0]
            and point[1] > bottom_left[1]
            and point[1] < top_right[1]
        ):
            return True
        else:
            return False

    def make_rocks(self, count):
        self.rocks = []
        counter = 0
        grid_size = SCREEN_X

        while counter < count:
            p1 = randrange(-grid_size, grid_size)
            p2 = randrange(-grid_size, grid_size)
            rock = Turtle("square")
            rock.color(self.color_name)
            rock.setpos(p1, p2)
            self.rocks.append(rock)
            counter += 1

        return self.rocks


player1 = Player("turtle")
player1.setup(color="green")
print(player1.color)

player2 = Player("turtle")
player2.setup(color="red")


screen.onkeypress(player1.turn_left, "Left")
screen.onkeypress(player1.turn_right, "Right")
screen.onkeypress(player2.turn_left, "a")
screen.onkeypress(player2.turn_right, "d")

screen.listen()

while True:
    player1.forward(1)
    player2.forward(1)

    player1.rock_check()
    player2.rock_check()

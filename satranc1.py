import turtle
from turtle import *


def main():
    boyut = int(input('Boyut girin: '))
    side = 50

    x_coord = -250
    y_coord = 300

    turtle = Turtle()
    turtle.speed('fastest')
    turtle.pensize(5)

    fill = False

    for i in range(boyut ** 2):
        if not i % boyut:
            y_coord -= side
            turtle.penup()
            turtle.setx(x_coord)
            turtle.sety(y_coord)
            turtle.pendown()
            if not boyut % 2:
                fill = not fill

        if fill:
            turtle.begin_fill()

        for _ in range(4):
            turtle.forward(side)
            turtle.right(90)

        turtle.forward(side)
        turtle.end_fill()
        fill = not fill


def exitonclick():
    pass


if __name__ == '__main__':
    main()
    exitonclick()

turtle.done()

import turtle

turtle.speed(0)

turtle.bgcolor("pink")



def donus():

    for i in range(200):

        turtle.right(1)

        turtle.forward(1)



turtle.color("red")



turtle.begin_fill()

turtle.left(140)

turtle.forward(111.65)

donus()



turtle.left(120)

donus()

turtle.forward(111.65)

turtle.end_fill()

turtle.hideturtle()
turtle.done()
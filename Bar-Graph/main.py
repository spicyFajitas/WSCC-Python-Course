import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
		
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height), font=("Arial",12 , "normal"))
    t.right(90)
    t.forward(25*2)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape


border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setup(width=600, height=600)
#wn.title("Welcome to the turtle zoo!")
wn.bgcolor("lightgreen")

turtle = turtle.Turtle()           # create turle and set some attributes

turtle.color("blue")
turtle.fillcolor("red")
turtle.pensize(3)
turtle.penup()
turtle.setx(-250)
turtle.sety(-300)
turtle.pendown()

drawBar(turtle, 40*2)
drawBar(turtle, 170*2)
drawBar(turtle, 200*2)
drawBar(turtle, 240*2)
drawBar(turtle, 160*2)
drawBar(turtle, 220*2)
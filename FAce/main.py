from turtle import *

#give an emotion in the assignment
import turtle

speed(8)
turtle.up()
turtle.goto(0, -100)  # center circle around origin
turtle.down()

turtle.begin_fill()
turtle.fillcolor("yellow")  # draw head
turtle.circle(100)
turtle.end_fill()

turtle.up()
turtle.goto(70, -40)
turtle.setheading(120)
turtle.width(5)
turtle.down()
turtle.circle(80, 120)  # draw smile

turtle.fillcolor("black")

for i in range(-35, 105, 70):
    turtle.up()
    turtle.goto(i, 35)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(10)  # draw eyes
    turtle.end_fill()




turtle.up()
turtle.goto(-50, 65)
turtle.setheading(-5)     #left eyebrow
turtle.width(5)
turtle.down()
turtle.forward(30)


turtle.up()
turtle.goto(20, 79)
turtle.setheading(2)			#right eyebrow
turtle.width(5)
turtle.down()
turtle.forward(30)

turtle.hideturtle()
turtle.done()
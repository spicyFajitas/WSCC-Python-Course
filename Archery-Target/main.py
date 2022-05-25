from turtle import *


wn=Screen()
wn.setup(height=900,width=700)
wn.bgcolor("lightgrey")

speed(0)

up()
goto(0,-250)
down()
begin_fill()
fillcolor("white")		#white ring
pencolor("White")
circle(250)
end_fill()
up()

goto(0,-200)
down()
begin_fill()
fillcolor("Black")		#black ring
pencolor("black")
circle(200)
end_fill()
up()

goto(0,-150)
down()
begin_fill()
fillcolor("Blue")		#blue ring
pencolor("blue")
circle(150)
end_fill()
up()

goto(0,-100)
down()
begin_fill()
fillcolor("Red")		#red ring
pencolor("red")
circle(100)
end_fill()
up()

goto(0,-50)
down()
begin_fill()
fillcolor("yellow")		#yellow circlew
pencolor("yellow")
circle(50)
end_fill()
up()

hideturtle()
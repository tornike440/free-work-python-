from turtle import*

setup(width=1.0, height=1.0) 
speed(4)
color("blue")
width(5)
bgcolor("light blue")

penup()
goto(-25,0)
pendown()

forward(50)

penup()
goto(25,25)
pendown()

right(90*3)
circle(25, extent=270)
right(90)


penup()
goto(-5,55)
pendown()

forward(20)

penup()
goto(5,55)
pendown()

forward(20)




exitonclick()
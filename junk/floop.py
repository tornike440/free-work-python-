from turtle import*

penup()
goto(0,-250)
pendown()
x=220

for i in range(0,10):
    if x % 40 == 0:
        color("green")
    else:
        color("yellow")




    begin_fill()
    circle(x)

    end_fill()

    x=x-20



exitonclick()
from turtle import*
import random
speed(100)

# def randColor():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     pencolor(r, g, b)
#go to starting point
penup()
goto(0,-250)
pendown()
x=0
for i in range(0,10):
    x=x+1
    y=360/x
    if x%2==1:
        color("blue")
    else:
        color("red")
    

    
    print(y)

    begin_fill()
    for i in range(0,int(y)):
        forward(5)
        left(x)
    end_fill()
    
    

    




exitonclick()
    







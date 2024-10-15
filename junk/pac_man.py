from turtle import*

speed(15)
bgcolor("dark blue")
color("yellow")

#drawing pacman
penup()
goto(-100,0)
pendown()
begin_fill()

left(90)
circle(100)

end_fill()

#pac man mouth 

penup()
goto(-200,0)
pendown()

right(60)
color("dark blue")
begin_fill()

forward(150)
right(120)
forward(150)

end_fill()

penup()
goto(-180,55)
pendown()

color("black")
begin_fill()

circle(10)

end_fill()

#drawing ghost

penup()
goto(250,-100)
pendown()
color("light blue")
begin_fill()


circle(30,extent=180)
right(180)
circle(30,extent=180)
right(180)
circle(30,extent=180)

forward(100)
circle(90,extent=180)

end_fill()

penup()
goto(285,0)
pendown()
color("white")
begin_fill()
circle(25)
end_fill()

penup()
goto(355,0)
pendown()
begin_fill()
circle(25)
end_fill()

color("red")
begin_fill()
circle(10)
end_fill()


penup()
goto(285,0)
pendown()
begin_fill()
circle(10)
end_fill()




penup()
goto(250,-100)
pendown()
color("black")


circle(30,extent=180)
right(180)
circle(30,extent=180)
right(180)
circle(30,extent=180)

forward(100)
circle(90,extent=180)
forward(100)


penup()
goto(285,0)
pendown()
circle(25)
circle(10)


penup()
goto(355,0)
pendown()
circle(25)
circle(10)



penup()
goto(0,-100)
pendown()
color("green")
begin_fill()


circle(30,extent=180)
right(180)
circle(30,extent=180)
right(180)
circle(30,extent=180)

forward(100)
circle(90,extent=180)
forward(100)

end_fill()

penup()
goto(35,0)
pendown()
color("white")
begin_fill()
circle(25)
end_fill()
color("blue")


begin_fill()
circle(10)
end_fill()

color("black")
circle(25)
circle(10)
color("white")
penup()
goto(95,0)
pendown()
begin_fill()
circle(25)
end_fill()

color("blue")
begin_fill()
circle(10)
end_fill()


color("black")
circle(25)
circle(10)


end_fill()




penup()
goto(0,-100)
pendown()
color("black")


circle(30,extent=180)
right(180)
circle(30,extent=180)
right(180)
circle(30,extent=180)

forward(100)
circle(90,extent=180)
forward(100)

penup()
goto(0,200)
pendown()
color("yellow")
left(90)
begin_fill()

forward(50)
left(90)
forward(20)
left(90)
forward(100)
left(90)
forward(21)

end_fill()

penup()
goto(70,180)
pendown()
color("yellow")
begin_fill()
left(90)

forward(25)
left(90)
forward(40)
right(120)
forward(20)
left(60)
forward(20)
right(120)
forward(40)
left(90)
forward(25)
left(90)
forward(80)
left(120)
forward(50)
right(60)
forward(50)

penup()
goto(70,180)
pendown()
right(60)
forward(80)

end_fill()
right(90)


penup()
goto(176,180)
pendown()
begin_fill()

forward(25)
left(60)
forward(25)
right(60)
forward(25)
right(60)
forward(25)
left(60)
forward(25)
left(120)
forward(100)
right(60)

end_fill()

right(135)


penup()
goto(296,180)
pendown()
color("Yellow")
begin_fill()

left(75)
forward(25)
left(90)
forward(40)
right(120)
forward(80)
left(120)
forward(80)
left(90)
forward(25)
left(90)
forward(40)
right(120)
forward(80)
left(120)




end_fill()



penup()
goto(220,217)
pendown()
color("dark blue")
begin_fill()
left(155)
forward(25)


right(135)
forward(25)

end_fill()


penup()
goto(-120,200)

color("yellow")
pendown()
begin_fill()
circle(40)
end_fill()

penup()
goto(-100,205)

color("dark blue")
pendown()
begin_fill()
circle(20)
end_fill()

penup()
goto(-85,192)

color("dark blue")
pendown()
begin_fill()

left(70)
forward(60)
left(90)
forward(40)
left(90)
forward(60)

end_fill()



color("yellow")
right(180)
penup()
goto(-220,180)
pendown()
begin_fill()

forward(25)
left(60)
forward(25)
right(60)
forward(25)
right(60)
forward(25)
left(60)
forward(25)
left(120)
forward(100)
right(60)

end_fill()



penup()
goto(-175,217)
pendown()
color("dark blue")
begin_fill()
left(7)
forward(25)

right(135)
forward(25)

left(60)
end_fill()

color("yellow")
penup()
goto(-240,200)
pendown()
begin_fill()
circle(30,extent=187)
forward(30)
left(90)
forward(80)
left(90)
forward(30)
end_fill()

color("dark blue")
penup()
goto(-240,210)
pendown()
begin_fill()
circle(20)
end_fill()


penup()
goto(-240,250)
pendown()
color("yellow")
right(180)
begin_fill()
circle(20,extent=180)
end_fill()









exitonclick()
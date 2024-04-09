from turtle import *
speed(40)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end


forward(70)                       #door
color ("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(160,175)
pendown()

color("brown")
left(30)
forward(40)

penup()
goto(140, 155)
pendown()
left(90)
forward(40)
penup()
goto(50,135)
pendown()
left(90)
forward(40)
penup()
goto(30, 155)
pendown()
right(90)
forward(40)


penup()
goto(30, 175)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

penup()
goto(140, 135)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)






exitonclick()
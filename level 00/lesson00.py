from turtle import*
#we want to paint a house
color("purple")
#drawing a square
speed(20)
width(7)
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
#end of square
#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(90)       #height of the door
right (90)
forward(60)
right(90)
forward(90)
end_fill()
#end of door
#drawing a roof

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
penup()
goto(200,200)
pendown()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(70,100)
pendown()
begin_fill()
color("blue")
right(60)
forward(60)   
right(90)
forward(80)
right(90)
forward(60)
right(90)
forward(80)
end_fill()

penup()
goto(190,130)
pendown()
begin_fill()
color("blue")
forward(30)
right(90)
forward(60)   
right(90)
forward(80)
right(90)
forward(60)
right(90)
forward(80)
end_fill()


exitonclick()
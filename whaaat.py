import  turtle
screen = turtle.Screen()
point = turtle.Turtle()
point.begin_fill()
point.fillcolor("yellow")

for i in  range(4):
    point.forward(100)
    point.right(90)

point.end_fill()
screen.exitonclick()
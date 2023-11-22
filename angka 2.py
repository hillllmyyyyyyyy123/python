import turtle
turtle.shape("turtle")
for i in range(0,3):
    turtle.forward(50)
    turtle.right(90)
    for i in range(0,4):
        turtle.forward(50)
        turtle.left(90)
turtle.exitenclick()
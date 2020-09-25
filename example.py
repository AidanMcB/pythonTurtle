from turtle import Screen, Turtle
TK_SILENCE_DEPRECATION=1
screen = Screen()

turtle = Turtle()

turtle.forward(100)
turtle.color('purple')
turtle.circle(50)
turtle.left(50)
turtle.forward(100)
turtle.color('blue')
turtle.right(50)
turtle.pensize(10)
turtle.forward(200)
turtle.stamp()
turtle.left(180)
turtle.forward(200)
screen.mainloop()
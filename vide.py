import turtle
a=0
b=0
turtle.speed(18)
turtle.bgcolor('blue')
turtle.pencolor('red')
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
while True:
  turtle.forward(a)
  turtle.right(b)
  a+=3
  b+=1
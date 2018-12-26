import turtle

play =turtle.Turtle()

turtle.shape('turtle')
turtle.shapesize(2,2,3)
turtle.fillcolor('red')

turtle.circle(30)
turtle.penup()
turtle.right(150)
turtle.forward(20)
turtle.pendown()
turtle.circle(50)
turtle.done() # 실행만 하고 종료되는걸 막음!!

from random import randint
import turtle

turtle.hideturtle()
turtle.penup()
turtle.speed(10)
turtle.goto(-300, 300)
turtle.pendown()
for i in range(4):
    turtle.forward(600)
    turtle.right(90)


number_of_turtles = 20
steps_of_time_number = 200
dt = 0.1

trtl_speed = []
pool = [turtle.Turtle(shape="circle", visible=False) for i in range(number_of_turtles)]

for unit in pool:
    unit.hideturtle()
    unit.shapesize(0.5)
    unit.penup()
    unit.goto(randint(-200, 200), randint(-200, 200))
    trtl_speed.append([randint(-20, 20), randint(-20, 20)])
    unit.showturtle()

for i in range(steps_of_time_number):
    for trtl in pool:
        trtl.goto(trtl.xcor()+trtl_speed[pool.index(trtl)][0]*dt, trtl.ycor()+trtl_speed[pool.index(trtl)][1]*dt)
        if int(trtl.xcor()) <= -300 or int(trtl.xcor()) >= 300:
            trtl_speed[pool.index(trtl)][0] = -trtl_speed[pool.index(trtl)][0]
        if int(trtl.ycor()) <= -300 or int(trtl.ycor()) >= 300:
            trtl_speed[pool.index(trtl)][1] = -trtl_speed[pool.index(trtl)][1]

input()

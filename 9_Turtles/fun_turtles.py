# Drawing class

import turtle

screen = turtle.Screen()
screen.bgcolor("#8FED90")

t = turtle.Turtle()
t.shape("turtle")
t.pensize(4)
t.color("#3265FB")
t.stamp()

def draw_line(line_size):
    t.pendown()
    t.forward(line_size)
    t.penup()


def draw_turtle():
    t.pendown()
    t.stamp()
    t.penup()

angle = 0

while angle < 360:
    angle_increment = 30
    distance = 100
    line_size = 10
    gap = 20

    t.penup()
    t.right(angle_increment)
    t.forward(distance)
    draw_line(line_size)
    t.forward(gap)
    draw_turtle()
    t.backward(distance + line_size + gap)
    t.pendown()

    angle += angle_increment

screen.exitonclick()

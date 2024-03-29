#!/usr/bin/env python
import turtle


t = turtle.Pen()
t.speed(0)

def head():

    t.penup()
    t.goto(0, (-100))
    t.pendown()
    t.begin_fill()
    t.fillcolor('gold')
    t.circle(100)
    t.end_fill()
    t.penup()

def glasses():

    # left frame
    t.penup()
    t.goto(20, 50)
    t.pencolor('brown')
    t.pensize(10)
    t.setheading(0)
    t.pendown()
    t.fillcolor('skyblue')
    t.begin_fill()
    t.forward(60)
    t.circle(8, 90)
    t.forward(30)
    t.circle(8, 90)
    t.forward(60)
    t.circle(8, 90)
    t.forward(30)
    t.circle(8, 90)
    t.end_fill()
    # right frame
    t.penup()
    t.goto((-20), 50)
    t.setheading(180)
    t.pendown()
    t.begin_fill()
    t.forward(60)
    t.circle((-8), 90)
    t.forward(30)
    t.circle((-8), 90)
    t.forward(60)
    t.circle((-8), 90)
    t.forward(30)
    t.circle((-8), 90)
    t.end_fill()
    # connect left and right
    t.penup()
    t.goto((-6), 70)
    t.setheading(0)
    t.pensize(20)
    t.pendown()
    t.forward(13)
    # left shining
    t.penup()
    t.goto(50, 65)
    t.setheading(45)
    t.pensize(8)
    t.pencolor('white')
    t.pendown()
    t.forward(25)
    t.penup()
    t.goto(70, 65)
    t.pendown()
    t.forward(12)
    # right shining
    t.penup()
    t.goto((-50), 65)
    t.setheading(45)
    t.pensize(8)
    t.pencolor('white')
    t.pendown()
    t.forward(25)
    t.penup()
    t.goto((-30), 65)
    t.pendown()
    t.forward(12)

def face():

    # left eye
    t.pencolor('black')
    t.pensize(5)
    t.penup()
    t.goto(55, 15)
    t.pendown()
    t.setheading(110)
    t.circle(20, 140)
    t.penup()
    # right eye
    t.goto((-55), 15)
    t.pendown()
    t.setheading(70)
    t.circle((-20), 140)
    t.penup()
    # outside mouse
    t.goto((-15), (-10))
    t.pensize(1)
    t.pencolor('coral')
    t.fillcolor('coral')
    t.setheading((-90))
    t.pendown()
    t.begin_fill()
    t.circle(15, 180)
    for i in range(10):
        t.forward(3)
        t.left(7)
    t.left(20)
    t.backward(2)
    t.left(20)
    for i in range(10):
        t.forward(3)
        t.left(7)
    t.end_fill()
    # inside mouse
    t.penup()
    t.goto(12, (-10))
    t.setheading(120)
    t.pencolor('darkred')
    t.fillcolor('darkred')
    t.begin_fill()
    t.circle(14, 120)
    t.setheading((-60))
    t.circle(14, 120)
    t.end_fill()

def hands():

    # left hand
    t.penup()
    t.goto(100, 0)
    t.pensize(1)
    t.pencolor('black')
    t.setheading((-10))
    t.pendown()
    t.fillcolor('gold')
    t.begin_fill()
    for i in range(7):
        t.forward(9)
        t.right(6)
    for i in range(19):
        t.forward(1)
        t.right(6)
    for i in range(7):
        t.forward(9)
        t.right(5)
    t.end_fill()
    # right hand
    t.penup()
    t.goto((-100), 0)
    t.setheading(190)
    t.pendown()
    t.fillcolor('gold')
    t.begin_fill()
    for i in range(7):
        t.forward(9)
        t.left(6)
    for i in range(19):
        t.forward(1)
        t.left(6)
    for i in range(7):
        t.forward(9)
        t.left(5)
    t.end_fill()

def hat():

    # blue part
    t.penup()
    t.goto(50, 96)
    t.pencolor('deepskyblue')
    t.fillcolor('deepskyblue')
    t.pensize(1)
    t.pendown()
    t.begin_fill()
    t.setheading(90)
    t.circle(10, 90)
    t.forward(10)
    t.setheading(90)
    t.forward(10)
    t.circle(5, 90)
    t.forward(50)
    t.circle(5, 90)
    t.forward(10)
    t.setheading(180)
    t.forward(10)
    t.circle(10, 90)
    t.setheading(0)
    t.forward(100)
    t.end_fill()
    # brown part
    t.penup()
    t.goto(20, 122)
    t.pencolor('brown')
    t.fillcolor('brown')
    t.setheading(90)
    t.pendown()
    t.begin_fill()
    t.forward(15)
    t.circle(5, 90)
    t.forward(30)
    t.circle(5, 90)
    t.forward(15)
    t.end_fill()

def draw():

    head()
    face()
    hat()
    glasses()
    hands()
    turtle.done()

draw()


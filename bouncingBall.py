#!/usr/bin/env python
import turtle
t = turtle.Pen()
t.speed(999)
turtle.bgcolor('black')
sides = 5
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
for x in range(360):
    t.pencolor(colors[(x % sides)])
    t.forward(((x * 3) / sides + x))
    t.left((360 / sides + 1))
    t.pensize(((x * sides) / 200))
    t.left(90)


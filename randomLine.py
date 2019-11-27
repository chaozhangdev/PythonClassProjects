#!/usr/bin/env python
import turtle
import random

t = turtle.Pen()
t.speed(100)
turtle.bgcolor('white')
colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'black', 'gray']
for n in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    x = random.randint((-300), 300)
    y = random.randint((-300), 300)
    t.penup()
    t.goto(x, y)
    t.pendown()
    for m in range(size):
        t.forward((m * 2))
        t.left(91)


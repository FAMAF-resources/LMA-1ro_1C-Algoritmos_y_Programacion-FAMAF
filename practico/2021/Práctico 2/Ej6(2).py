from turtle import *
from random import choice

bgcolor("yellow")
color(choice(['orange', 'red', 'green', 'blue', 'purple', 'grey', 'black']))
speed(13)
pensize(4)

for var1 in range(3):
    forward(100)
    right(120)

color(choice(['orange', 'red', 'green', 'blue', 'purple', 'grey', 'black']))

right(90)

for var2 in range(3):
    forward(100)
    right(120)

done()
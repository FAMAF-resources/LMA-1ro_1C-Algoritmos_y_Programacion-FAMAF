from turtle import *
from random import choice

bgcolor("yellow")
color(choice(['orange', 'red', 'green', 'blue', 'purple', 'grey', 'black']))

for var1 in range(4):
    for var2 in range(3):
        forward(100)
        right(120)
    right(90)

done()
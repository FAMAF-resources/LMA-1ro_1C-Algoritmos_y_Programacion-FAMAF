from turtle import *
from random import choice

bgcolor("yellow")
pensize(3)

for _ in range (8):
    color(choice(['orange', 'red', 'green', 'blue', 'purple', 'grey', 'black']))
    forward(100)
    backward(100)
    right(45)
done()
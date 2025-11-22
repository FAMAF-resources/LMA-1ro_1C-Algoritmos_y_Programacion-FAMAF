from turtle import *
from random import choice

speed(13)
bgcolor("yellow")
for var1 in range(36):
    color(choice(['orange', 'red', 'green', 'blue', 'purple', 'grey', 'black']))
    for var2 in range(3):
        forward(100)
        right(120)
    right(10)

done()
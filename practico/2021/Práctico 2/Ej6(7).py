from turtle import *
from random import choice

bgcolor("yellow")
color(choice(['orange', 'red', 'green', 'blue', 'purple', 'grey', 'black']))

for var1 in range(10):
    for var2 in range(4):
        forward(20)
        right(90)
    forward(20)

done()
















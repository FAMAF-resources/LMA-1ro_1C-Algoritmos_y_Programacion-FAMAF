from turtle import *
from random import choice

bgcolor("yellow")
speed(13)
pensize(5)

for var1 in range(4):
    for var2 in range(10):
        color(choice(['orange', 'red', 'green', 'blue', 'purple', 'grey', 'black']))
        for var3 in range(4):
            forward(20)
            right(90)
        forward(20)
    right(90)    

done()
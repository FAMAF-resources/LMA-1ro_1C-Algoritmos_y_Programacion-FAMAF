from turtle import *
from math import pi

bgcolor("yellow")
pensize(3)
color("green")
speed (3)

for _ in range (4):
    forward(360/pi)
    right(90)

forward(180/pi)

color("black")

for _ in range(360):
    forward(1)
    right(1)

done()
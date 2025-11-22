#Se calcula el area de un circulo dado su perimetro
import math

def area_circulo (perimetro_circulo):
    radio = (perimetro_circulo)/(math.pi*2)
    return math.pi*(radio**2)

print(area_circulo(18.84))
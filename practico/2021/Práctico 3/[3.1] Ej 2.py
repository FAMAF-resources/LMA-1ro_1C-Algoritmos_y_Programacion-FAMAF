#Se sabe el lado mas corto del rectangulo.
#El lado mas grande mide el doble que el menor.
#Cada lado se repite 2 veces por lo tanto se multiplica por dos.
#Uno de los lados es del doble que el otro entonces se multiplica nuevamente por 2.

def perimetro_rectangulo (lado):
    return lado*2 + lado*2*2

print(perimetro_rectangulo(5))
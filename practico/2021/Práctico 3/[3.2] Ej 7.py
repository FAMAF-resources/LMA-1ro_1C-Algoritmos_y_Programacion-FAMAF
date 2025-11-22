def valor_absoluto (num):
    if num >= 0:
        num = num
    else:
        num = num*(-1)
    return num

def orden_de_magnitud (num1, num2):
    if valor_absoluto(num1) > valor_absoluto(num2):
        print('El módulo de', num1, 'es mayor que el módulo de', num2)
    elif valor_absoluto(num1) < valor_absoluto(num2):
        print('El módulo de', num2, 'es mayor que el módulo de', num1)
    else:
        print('Los modulos de los números son iguales')

orden_de_magnitud(4,-7)
def relacion_de_un_cuadrado(num1, num2):
    if num1**2 < num2:
        print(num1, 'elevado al cuadrado es menor a', num2)
    elif num1**2 == num2:
        print(num1, 'elevado al cuadrado es igual a', num2)
    else:
        print(num1, 'elevado al cuadrado es mayor', num2)

relacion_de_un_cuadrado(3,10)
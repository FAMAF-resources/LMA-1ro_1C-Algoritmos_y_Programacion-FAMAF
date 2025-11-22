def es_bisiesto(anho: int):
    return anho % 4 == 0 and (anho % 100 != 0 or anho % 400 == 0)

def fecha_valida (fecha: tuple):
    dia, mes, año = fecha
    
    if año <= 1970:
        print('Año fuera de rango')

    if mes in [4, 6, 9, 11]:
        if dia > 30 or dia < 1:
            print('Dia fuera de rango')
    elif mes == 2:
        if dia > 29 or dia < 1:
            print('Dia fuera de rango')
        elif dia == 29 and es_bisiesto(año) == False:
            print('Dia fuera de rango')
    elif mes in [1, 3, 5, 7, 8, 10, 12]:   
        if dia > 31 or dia < 1:
            print('Dia fuera de rango')
    else:
        print('Mes fuera de rango')


print(fecha_valida((29,12,1997)))

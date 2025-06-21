def es_bisiesto(anho: int):
    if anho % 4 == 0 and (anho % 100 != 0 or anho % 400 == 0):
        print(anho, 'es un año bisiesto')
    else:
       print(anho, 'no es un año bisiesto') 

print(es_bisiesto(1996))
#Dado una cierta cantidad de chocolates se calcula cuanto recibirá cada alumno.
#Los chocolates no se pueden partir.

def administracion_chocolates (chocolates, estudiantes):
    return chocolates // estudiantes

print(administracion_chocolates(12,4))
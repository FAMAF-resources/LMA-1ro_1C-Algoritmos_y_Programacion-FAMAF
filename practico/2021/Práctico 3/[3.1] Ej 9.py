#Despues de dividir los chocolates entre los alumnos los que sobran son para los profes.
def chocolates_de_profes (chocolates, estudiantes):
    return chocolates % estudiantes

print(chocolates_de_profes(7,4))
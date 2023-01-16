# Convertir un objeto Series a una lista Python.

import pandas as pd

datos = [2, 3, 5, 7, 11]

serie = pd.Series(datos)

# Averiguar el tipo de dato de la variables "datos"
print(type(datos))

# Averiguar el tipo de dato de la variable "serie"
print(type(serie))

# Convertir el objeto "Serie" a "Lista"
lista = serie.tolist()
print(type(lista))
print(lista)

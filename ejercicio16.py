# Obtener la desviacion estandar y el promedio de un conjunto de datos de una serie.

import pandas as pd

datos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

serie = pd.Series(datos)

print(serie)

# Funcion para obtener la desviacion estandar
print(serie.std())

# Funcion para obtener el promedio
print(serie.mean())
# Crear y visualizar un arreglo unidimensional como una estructura Series

import pandas as pd

datos = [2, 3, 5, 7, 11]

serie = pd.Series(datos)

print(serie)

# Imprimir la cantidad de elementos con .size
print(serie.size)

# Nos devuelve estadisticas basicas sobre los datos de la lista.
print(serie.describe())

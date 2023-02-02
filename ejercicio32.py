# Contar los valores repetidos en una serie.

import pandas as pd

datos = [5, 3, 5, 7, 7, 3, 1, 2, 3, 0]

serie = pd.Series(datos)
print("\nEjemplo 01")
print(serie)

# Identificamos los ducplicados con el metodo "value_counts"
print("\nEjemplo 02")
print(serie.value_counts())


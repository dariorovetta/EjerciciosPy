# Obtener los primeros y últimos n elementos de un objeto Series.

import pandas as pd

datos = list(range(1, 101))

serie = pd.Series(datos)
print("\nEjemplo 01")
print(serie)

# Mostrar los primeros elementos de una lista, con el método ".head()".
print("\nEjemplo 02")
print(serie.head(7))

# Mostrar los últimos elementos de una lista, con el método ".tail()".
print("\nEjemplo 03")
print(serie.tail(5))


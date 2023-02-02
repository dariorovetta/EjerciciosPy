# Remover los valores que no cumplan una condicion en un objeto Series

import pandas as pd

datos = list(range(1, 11))

serie = pd.Series(datos)
print("\nEjemplo 01")
print(serie)

# Remover todos los elementos que sean menor a 5
print("\nEjemplo 02")
print(serie.where(serie >= 5).dropna())

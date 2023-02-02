# Generar representacion JSON de un objeto Series.

import pandas as pd

datos = [1, 2, 3, 4, 5]

serie = pd.Series(datos)
print("\nEjemplo 01")
print(serie)

# Convertimos una serie en JSON
print("\nEjemplo 02")
print(serie.to_json())

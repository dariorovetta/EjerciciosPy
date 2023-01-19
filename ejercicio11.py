# Convertir un objeto Series con multiples listas en un único objeto Series.

import pandas as pd

datos = [["Colombia", "Peru"], ["Bolivia", "Uruguay"], ["Chile"]]

serie = pd.Series(datos)
print(serie)

# .apply() sirve para aplicar una funcion a lo largo de un DataFrame
# Unificamos las listas de la Serie en una sola Serie
serie = serie.apply(pd.Series).stack().reset_index(drop=True)
print(serie)
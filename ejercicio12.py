# Ordenar los valores de un objeto Series con el metodo sort_values.

import pandas as pd

datos = ["1.1", "Python", "0.5", "pandas", "2.8"]

serie = pd.Series(datos)
print(serie)

orden = serie.sort_values()
print(orden)

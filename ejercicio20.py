# Extraer los datos de un objetos Series como un objeto NumPy.

import pandas as pd

datos = list(range(10))

serie = pd.Series(datos)

print(serie)

numpy = serie.values
print(numpy)


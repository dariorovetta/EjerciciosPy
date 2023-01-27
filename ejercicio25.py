# Calcular el valor absoluto de los elementos de un objeto Series.

import pandas as pd

datos = [-5, 3, 0, -8, 1, 3, -7]

serie = pd.Series(datos)
print(serie)

# Obtener el valor absoluto
print(serie.abs())
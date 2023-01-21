# Calcular los valores mínimos y maximo de un objeto Series

import pandas as pd

datos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

serie = pd.Series(datos)

# Obtener el valor mínimo
print(serie.min())

# Obtener el valor máximo
print(serie.max())
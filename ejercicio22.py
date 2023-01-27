# Obtener el tamaño en bytes del espacio ocupado por los elementos de un objeto Series.

import pandas as pd

datos = list(range(10))
print(datos)

serie = pd.Series(datos)
print(serie)

# Calcular el espacio ocupado
print()
print(serie.nbytes)


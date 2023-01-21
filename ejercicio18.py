# Obtener estadisticas básicas de un objeto Series con el método describe.

import pandas as pd

# Crear una lista con los número del 0 al 9
datos = list(range(10))

serie = pd.Series(datos)

# Mostrar estadistica basica de la serie
print(serie.describe())
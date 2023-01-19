# Crear un objeto Series a partir de un filtro aplicado a otro objeto Series.

import pandas as pd

datos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

serie = pd.Series(datos)
print(serie)

n = 6

# Al poner la condicion de esta forma, va a evaluar valor por valor.
serieNueva = serie[serie < n]
print(serieNueva)
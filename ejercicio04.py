# Aplicar las operaciones aritmeticas basicas sobre Series.

import pandas as pd

serie1 = pd.Series([1, 2, 3, 4, 5])
serie2 = pd.Series([9, 8, 7, 6, 5])

# Al realizar operaciones entre series, se hacen entre los valores que esten
# en la misma ubicacion. --> Por ejemplo: 1 + 9, 2 + 8, etc...

# Suma de dos series
suma = serie1 + serie2
print(suma)

# Resta de dos series
resta = serie1 - serie2
print(resta)

# Multiplicación de dos series
multiplicacion = serie1 * serie2
print(multiplicacion)

# División de dos series
division = serie1 / serie2
print(division)

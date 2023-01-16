# Usar operadores relacionales para comparar objetos Series.

import pandas as pd

serie1 = pd.Series([1, 2, 3, 5, 7])
serie2 = pd.Series([13, 17, 11, 5, 3])

# Comparacion menor entre dos series
comparacion = serie1 < serie2
print(comparacion)

# Comparacion mayor entre dos series
comparacion = serie1 > serie2
print(comparacion)

# Comparacion igual entre dos series
comparacion = serie1 == serie2
print(comparacion)
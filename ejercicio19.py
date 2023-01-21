# Obtener los elementos pares e impares de un objeto Series.

import pandas as pd

datos = list(range(10))

serie = pd.Series(datos)

# Selecionar los números que su módulo es igual a 0 (pares)
pared = serie[serie % 2 == 0]
print(pared)

# Selecionar los números que su módulo es distinto a 0 (impares)
pared = serie[serie % 2 != 0]
print(pared)
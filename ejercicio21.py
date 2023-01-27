# Comprobar si una serie de elementos contienen valores numericos.

import pandas as pd

datos = ["20", "30", "Python", "50", "100"]

serie = pd.Series(datos)
print(serie)

# Verificar si los elementos son números
serie = pd.to_numeric(serie, errors="coerce")
print(serie)

# verificar si en los elementos hay algun NaN
print()
print(serie.hasnans)

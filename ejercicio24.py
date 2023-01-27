# Elimina los valores NaN de una serie con el método dropna

import pandas as pd
import numpy as np

datos = ["2.3", "Python", "90", "100", np.nan, "0.5", ".9"]

serie = pd.Series(datos)
print(serie)

# Verificar si elementos de la lista son numeros. Si se muestra error, deja NaN.
serie = pd.to_numeric(serie, errors="coerce")
print(serie)

# Eliminar elentos "NaN" de una serie
serie = serie.dropna()
print(serie)


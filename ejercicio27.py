# Reemplazar los valores NaN (null) de una serie con un valor arbitrario.

import pandas as pd
import numpy as np

datos = [1, 3, 7, 11, "Python", "-0.5", np.nan]

serie = pd.Series(datos)
print(serie)

# Convertir los elementos a número y si no son números se convierten en NaN
serie = pd.to_numeric(serie, "coerce")
print(serie)

# Reemplazar elementos NaN por 0
serie.fillna(0, inplace=True) # inplace es para sobreescribir los valores de "serie"
print(serie)

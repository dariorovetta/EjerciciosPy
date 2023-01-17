# Convertir un arreglo NumPy en un objeto Series.

import numpy as np
import pandas as pd

arreglo = np.array([2, 3, 5, 7, 11])
print(arreglo)

# Pasar de Numpy a Series
serie = pd.Series(arreglo)
print(serie)
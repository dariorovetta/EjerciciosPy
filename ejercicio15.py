# Cambiar el orden del indice de un objeto Series.

import pandas as pd

datos = [1, 2, 3, 4, 5]

indices = ["A", "B", "C", "D", "E"]

# Creamos una serie indicando los datos y el indice a pasar
serie = pd.Series(data=datos, index=indices)
print(serie)

# Cambiamos el orden de los indices
serie = serie.reindex(index=["B", "A", "C", "D", "E"])
print(serie)
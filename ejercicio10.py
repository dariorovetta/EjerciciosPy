# Extraer una fila de un DataFrame como un objeto Series

import pandas as pd

datos = {"A": [1, 2, 3, 4, 5], "B": [6, 5, 4, 3, 2], "C": [2, 3, 5, 7, 11]}

df = pd.DataFrame(data=datos)

fila = df.iloc[2]

print(fila)



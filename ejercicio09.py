# Obtener una columna de un objeto DataFrame como un objeto Series.

import pandas as pd

datos = {"A":[1, 2, 3, 4, 5],
         "B":[9, 8, 7, 6, 5],
         "C":[2, 3, 5, 7, 11]}

# Creamos un DataFrame con un diccionario.
# Utilizando el atributo "data=" y seleccionamos el diccionario
df = pd.DataFrame(data=datos)
print(df)

# Tipo de dato de este objeto
print(type(df))

# Extraemos una columna del DataFrame con el metodo ".iloc"
columna = df.iloc[:, 1]
print(columna)

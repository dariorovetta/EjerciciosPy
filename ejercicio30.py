# Reemplazar por un valor arbritario los valores de una serie que no satisfagan una condicion

import pandas as pd

datos = list(range(1, 6))

serie = pd.Series(datos)
print("\nEjemplo 01")
print(serie)

# Los valores que no cumplen la condicion quedan como NaN, utilizando ".where()"
print("\nEjemplo 02")
print(serie.where(serie > 1))

# Podemos editar el valor que devuelve cuando no se cumple la condicion. Agregando otro atributo despues de la condicion.
print("\nEjemplo 03")
print(serie.where(serie > 1, -1))

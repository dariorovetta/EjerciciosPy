# Obtener la representación de diccionario de un objeto Series.

import pandas as pd

capitales = ["Buenos Aires", "Lima", "Paris", "Berlin", "Madrid"]
paises = ["Argentina", "Peru", "Francia", "Alemania", "España"]

# Creamos el objeto series e indicamos que utilizar como indice
serie = pd.Series(capitales, index=paises)
print("\nEjemplo 01")
print(serie)

# Transformar la serie en diccionario
print("\nEjemplo 02")
print(serie.to_dict())
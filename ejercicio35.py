# Crear un objeto DataFrame a partir de un objeto Series
import pandas as pd

capitales = ["Buenos Aires", "Lima", "Paris", "Berlin", "Madrid"]
paises = ["Argentina", "Peru", "Francia", "Alemania", "España"]

# Creamos el objeto series e indicamos que utilizar como indice
serie = pd.Series(capitales, index=paises)
print("\nEjemplo 01")
print(serie)

# Convertimos la serie en Dataframe
print("\nEjemplo 02")
df = serie.to_frame()
print(df)

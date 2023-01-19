# Agregar datos a un objeto Series existente.

import pandas as pd

datos = ["Python", "C#", "C++", "Java", "PHP"]

serie = pd.Series(datos)
print(serie)

# Agregamos mas elementos, de la misma forma que se hacen en las listas
serie = serie.append(pd.Series(["JavaScripts", "Perl"])).reset_index(drop=True)
print(serie)
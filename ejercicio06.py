# Convertir un diaccionario Python en un objeto Series

import pandas as pd

dicc = {
    "Nombre":"Dario",
    "Apellido":"Rovetta",
    "Edad": 28,
    "Signo": "Virgo"
        }


# Pasar el diccionario a Series
# En este caso no se crean los indices automaticos
serie = pd.Series(dicc)
print(serie)

# Imprimir el valor que contiene "Nombre"
print("\nEl nombre es: " + serie["Nombre"])
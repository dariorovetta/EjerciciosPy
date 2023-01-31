# Usar la funcion de agregación agg de un objet Series.

import pandas as pd
from math import sqrt
import numpy as np

datos = [-8, 7, -6, 5, 0, 3, 7]

serie = pd.Series(datos)
print("Ejemplo 01")
print(serie)

# Obtener el valor máximo del objeto series
print("\nEjemplo 02")
print(serie.agg(max))

# Obtener el valor mínimo del objeto series
print("\nEjemplo 03")
print(serie.agg(min))

# Obtener el valor absoluto de los elementos de la serie
print("\nEjemplo 04")
print(serie.agg(abs))

# Utilizamos el metodo "sqrt" para obtener la raiz de los valores absolutos
print("\nEjemplo 05")
print(serie.agg(abs).agg(sqrt))

# Utilizamos el metodo "hex" para obtener el numero hexadecimal de los valores absolutos
print("\nEjemplo 06")
print(serie.agg(abs).agg(hex))

# Funcion para obtener el cuadrado de un número
print("\nEjemplo 07")
def cuadrado(x):
    return x * x

# Utilizar la funcion recien creada para todos los elementos de la serie
print(serie.agg(cuadrado))

# Las expresiones lambda también se conocen como funciones anónimas.
# Las expresiones lambda en Python son una forma corta de declarar funciones pequeñas.
# Las funciones Lambda se comportan como funciones normales declaradas con la palabra clave def.
print("\nEjemplo 08")
print(serie.agg(lambda x: x ** 3))

# Calcular el seno de cualquier elemento
print("\nEjemplo 09")
print(serie.agg(np.sin))

# Calcular la raiz cubica de cualquier elemento
print("\nEjemplo 10")
print(serie.agg(np.cbrt))

# Suma de todos los elementos que tenemos en la serie original.
print("\nEjemplo 11")
print(serie.agg(np.sum))

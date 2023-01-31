# Usar operadores relacionales con métodos de la clase Series.

import pandas as pd

datos1 = [1, 2, 3, 4, 5]
datos2 = [5, 4, 3, 2, 1]

serie1 = pd.Series(datos1)
serie2 = pd.Series(datos2)

print("\nEjemplo 01")
print(serie1)
print(serie2)

# "lt" sirve como el operador "menor que" --> "<"
print("\nEjemplo 02")
print(serie1.lt(serie2))

# "le" sirve como el operador "menor o igual que" --> "<="
print("\nEjemplo 03")
print(serie1.le(serie2))

# "eq" sirve como el operador "igual que" --> "=="
print("\nEjemplo 04")
print(serie1.eq(serie2))

# "ne" sirve como el operador "distinto que" --> "!="
print("\nEjemplo 05")
print(serie1.ne(serie2))

# "gt" sirve como el operador "mayor que" --> ">"
print("\nEjemplo 06")
print(serie1.gt(serie2))

# "ge" sirve como el operador "mayor o igual que" --> ">="
print("\nEjemplo 07")
print(serie1.ge(serie2))
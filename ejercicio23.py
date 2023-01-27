# Operaciones aritmetricas con métodos de la clase Serie: add, subtract, multiply y divide

import pandas as pd

serie1 = pd.Series(list(range(1, 11)))
print(serie1)

serie2 = pd.Series(list(range(10, 0, -1)))
print(serie2)

# Sumar dos series
print(serie1.add(serie2))

# Restar dos series
print(serie1.subtract(serie2))

# Multiplicar dos series
print(serie1.multiply(serie2))

# Dividir dos series
print(serie1.divide(serie2))
# 

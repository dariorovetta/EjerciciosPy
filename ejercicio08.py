# Cambiar el tipo de datos de un objeto Series.

import pandas as pd

datos = pd.Series(["100", "200", "python", "300.15", "500.8"])
print(datos)

# Pasamos el objeto a numerico con la funcion "to_numeric"
# En los parametros, primero va el objeto y despues que hacer con los errores
# En este caso usamos "coerce", para que cuando haya un error indique "NaN"
datos = pd.to_numeric(datos, errors="coerce")
print(datos)

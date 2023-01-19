# --- Importar pandas (01)
# import pandas as pd

# --- Verificar version de pandas (01)
# print(pd.__version__)

# --- Pasar una lista a formato Serie (02)
# pd.Series(lista)

# --- Imprimir la cantidad de elementos de la serie (02)
# serie  = pd.Series(lista)
# print(serie.size)

# --- Nos devuelve estadisticas basicas sobre los datos de la lista (02)
# print(serie.describe())

# --- Averiguar el tipo de dato de una variable (02)
#print(type(variable))

# --- Convertir un objeto "Serie" a "Lista" (03)
# serie.tolist()

# --- Operaciones con series (04)
# Cuando se hace una operacion entre series, se hace con el valor del mismo indice.
# suma = serie1 + serie2 
# suma = serie1 - serie2

# --- Comparaciones con series (05)
# Cuando se hace una comparacion entre series, se hace con el valor del mismo indice.
# comparacion = serie1 < serie2
# comparacion = serie1 > serie2

# --- Pasar diccionario a serie (06)
# serie = pd.Series(dicc)

# --- Convertir un arreglo NumPy en un objeto Series (07)
# arreglo = np.array([2, 3, 5, 7, 11])
# serie = pd.Series(arreglo)

# --- Pasar el objeto de Strings a valores numericos (08)
# datos = pd.to_numeric(datos, errors="coerce")

# --- Crear DataFrame con diccionario (09)
# df = pd.DataFrame(data=datos)



import pandas as pd
print(pd.__version__)

dataFrame = pd.read_csv(r'C:\Users\auriascos\PycharmProjects\AnalisisDatosPython\archivos\dataframe.csv')

print(dataFrame)

# Mostrar columnas o series cuando hay espacios en el nombre de la columna
print(dataFrame['Nombre'])

# Otra forma que no sirve si hay espacios
print(dataFrame.Pais)

# Mostrar dos series
print(dataFrame[['Edad', 'Automovil']])

# Verificar que es una serie, tipo "series"
print(type(dataFrame.Pais))

# Es un nuevo dataframe, tipo "DataFrame"
print(type(dataFrame[['Edad', 'Automovil']]))

# Conocer filas y columnas
print(dataFrame.shape)
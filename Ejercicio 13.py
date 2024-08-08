import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes, filtra los estudiantes
# que tienen una calificación mayor o igual a 80 en "Mat_CalculoIntegral" o mayor a 80 en
# "Mat_EstructuraDatos", y muestra los nombres de estos estudiantes.

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Filtrar los estudiantes según las condiciones especificadas
estudiantes_filtrados = df[(df['Mat_CalculoIntegral'] >= 80) | (df['Mat_EstructuraDatos'] > 80)]

# Mostrar los valores del campo "Nombre" de los estudiantes filtrados
nombres_estudiantes = estudiantes_filtrados['Nombre']

# Imprimir los nombres
print("Los nombres de los estudiantes con calificaciones mayores o iguales a 80 en 'Mat_CalculoIntegral' o mayores a 80 en 'Mat_EstructuraDatos' son:")
print(nombres_estudiantes)
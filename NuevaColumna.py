# Este programa lee un archivo de Excel llamado "calificaciones_alumnos.xlsx" que contiene
# las calificaciones de los alumnos en varias materias, agrega una nueva columna llamada
# 'Mat_Fisica' con valores aleatorios entre 0 y 100 con un decimal, y guarda el archivo
# actualizado.

import pandas as pd
import numpy as np

# Leer el archivo de Excel y cargarlo en un DataFrame
df = pd.read_excel('calificaciones_alumnos.xlsx', engine='openpyxl')

# Generar valores aleatorios entre 0 y 100 con un decimal para la columna 'Mat_Fisica'
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, size=len(df)), 1)

# Guardar el DataFrame actualizado en el mismo archivo de Excel
df.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False, engine='openpyxl')

# Informar al usuario que el proceso ha finalizado
print("Se ha añadido la columna 'Mat_Fisica' con valores aleatorios y se ha guardado el archivo actualizado.")
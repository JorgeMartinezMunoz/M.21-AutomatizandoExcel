# Este programa lee un archivo de Excel llamado "calificaciones_alumnos.xlsx" que contiene
# las calificaciones de los alumnos en varias materias. Agrega una nueva columna llamada
# 'Mat_Fisica' con valores aleatorios entre 0 y 100 con un decimal, ordena la tabla por
# el campo 'Nombre', guarda el archivo actualizado, imprime la cantidad de registros y campos,
# e identifica qué campos son numéricos.

import pandas as pd
import numpy as np

# Leer el archivo de Excel y cargarlo en un DataFrame
df = pd.read_excel('calificaciones_alumnos.xlsx', engine='openpyxl')

# Generar valores aleatorios entre 0 y 100 con un decimal para la columna 'Mat_Fisica'
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, size=len(df)), 1)

# Ordenar el DataFrame por la columna 'Nombre'
df = df.sort_values(by='Nombre')

# Obtener el número de registros (filas) y campos (columnas)
num_registros = len(df)
num_campos = len(df.columns)

# Imprimir la cantidad de registros y campos
print(f"La tabla tiene {num_registros} registros y {num_campos} campos.")

# Identificar los campos numéricos
campos_numericos = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"Los campos numéricos son: {campos_numericos}")

# Guardar el DataFrame actualizado en un nuevo archivo de Excel
df.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False, engine='openpyxl')

# Informar al usuario que el proceso ha finalizado
print("Se ha añadido la columna 'Mat_Fisica' con valores aleatorios, se ha ordenado por 'Nombre', se ha guardado el archivo actualizado y se han identificado los campos numéricos.")
import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes, calcula el promedio de las calificaciones,
# elimina los registros cuyo promedio es menor a 65 y guarda el resultado en un nuevo archivo Excel.

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Calcular el promedio de las calificaciones por estudiante
df['Promedio'] = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].mean(axis=1)

# Filtrar los registros cuyo promedio es mayor o igual a 65
df_filtrado = df[df['Promedio'] >= 65]

# Guardar el DataFrame filtrado en un nuevo archivo Excel
df_filtrado.to_excel('calificaciones_filtradas.xlsx', index=False)

print("Los registros cuyo promedio es menor a 65 han sido eliminados y el resultado se ha guardado como 'calificaciones_filtradas.xlsx'")
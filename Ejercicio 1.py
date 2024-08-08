import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Calcular el promedio de calificaciones para cada estudiante
# Primero, seleccionamos las columnas de calificaciones
calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']]

# Calculamos el promedio por estudiante
df['Promedio'] = calificaciones.mean(axis=1)

# Guardar el DataFrame con el promedio en un nuevo archivo Excel
df.to_excel('calificaciones_con_promedio.xlsx', index=False)

print("Cálculo de promedios completado y guardado en 'calificaciones_con_promedio.xlsx'")
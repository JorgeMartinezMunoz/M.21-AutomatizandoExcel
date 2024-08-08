import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes, calcula el promedio
# general de calificaciones por estudiante y guarda los resultados en un nuevo archivo Excel.
# También determina el estudiante con el mayor promedio y el estudiante con el menor promedio.

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Calcular el promedio de calificaciones para cada estudiante
# Primero, seleccionamos las columnas de calificaciones
calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']]

# Calculamos el promedio por estudiante
df['Promedio'] = calificaciones.mean(axis=1)

# Determinar el nombre del estudiante con el mayor promedio
estudiante_mejor_promedio = df.loc[df['Promedio'].idxmax(), 'Nombre']

# Determinar el nombre y promedio del estudiante con el menor promedio
estudiante_peor_promedio = df.loc[df['Promedio'].idxmin(), ['Nombre', 'Promedio']]

# Guardar el DataFrame con el promedio en un nuevo archivo Excel
df.to_excel('calificaciones_con_promedio.xlsx', index=False)

print("Cálculo de promedios completado y guardado en 'calificaciones_con_promedio.xlsx'")
print(f"El estudiante con el mayor promedio es: {estudiante_mejor_promedio}")
print(f"El estudiante con el menor promedio es: {estudiante_peor_promedio['Nombre']} con un promedio de {estudiante_peor_promedio['Promedio']:.2f}")
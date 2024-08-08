import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes, cuenta cuántos
# estudiantes tienen una calificación mayor o igual a 70 en la materia "Mat_CalculoIntegral"
# y calcula el porcentaje que representan respecto al total de estudiantes.

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Contar el número de estudiantes con calificación mayor o igual a 70 en "Mat_CalculoIntegral"
estudiantes_mayor_igual_70 = df[df['Mat_CalculoIntegral'] >= 70].shape[0]

# Contar el número total de estudiantes
total_estudiantes = df.shape[0]

# Calcular el porcentaje de estudiantes con calificación mayor o igual a 70
porcentaje_mayor_igual_70 = (estudiantes_mayor_igual_70 / total_estudiantes) * 100

# Imprimir el número de estudiantes y el porcentaje
print(f"El número de estudiantes con una calificación mayor o igual a 70 en 'Mat_CalculoIntegral' es: {estudiantes_mayor_igual_70}")
print(f"Esto representa el {porcentaje_mayor_igual_70:.2f}% del total de estudiantes.")
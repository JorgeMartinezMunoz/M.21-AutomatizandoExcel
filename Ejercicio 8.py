import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes y cuenta cuántos
# estudiantes tienen una calificación mayor a 70 en la materia "Mat_CalculoIntegral".

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Contar el número de estudiantes con calificación mayor a 70 en "Mat_CalculoIntegral"
estudiantes_mayor_70 = df[df['Mat_CalculoIntegral'] > 70].shape[0]

# Imprimir el número de estudiantes
print(f"El número de estudiantes con una calificación mayor a 70 en 'Mat_CalculoIntegral' es: {estudiantes_mayor_70}")
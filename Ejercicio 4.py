import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes y calcula el promedio
# de todas las calificaciones para la materia "Mat_CalculoIntegral".

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Seleccionar la columna de calificaciones para la materia "Mat_CalculoIntegral"
calificaciones_calculo_integral = df['Mat_CalculoIntegral']

# Calcular el promedio de las calificaciones de "Mat_CalculoIntegral"
promedio_calculo_integral = calificaciones_calculo_integral.mean()

# Imprimir el promedio calculado
print(f"El promedio de calificaciones para 'Mat_CalculoIntegral' es: {promedio_calculo_integral:.2f}")
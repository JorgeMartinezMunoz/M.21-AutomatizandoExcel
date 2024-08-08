import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes, calcula el promedio
# de calificaciones para la materia "Mat_CalculoIntegral", y ordena el archivo por la materia
# "Mat_ProgramacionOOP". Luego guarda el DataFrame ordenado en un nuevo archivo Excel.

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Calcular el promedio de las calificaciones de "Mat_CalculoIntegral"
calificaciones_calculo_integral = df['Mat_CalculoIntegral']
promedio_calculo_integral = calificaciones_calculo_integral.mean()

# Ordenar el DataFrame por la materia "Mat_ProgramacionOOP" en orden descendente
df_ordenado = df.sort_values(by='Mat_ProgramacionOOP', ascending=False)

# Guardar el DataFrame ordenado en un nuevo archivo Excel
df_ordenado.to_excel('calificaciones_ordenadas.xlsx', index=False)

# Imprimir el promedio calculado
print(f"El promedio de calificaciones para 'Mat_CalculoIntegral' es: {promedio_calculo_integral:.2f}")
print("El archivo ha sido ordenado por 'Mat_ProgramacionOOP' y guardado como 'calificaciones_ordenadas.xlsx'")
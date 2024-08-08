import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes, ordena el archivo
# por la materia "Mat_EstructuraDatos" en orden ascendente y guarda el DataFrame ordenado
# en un nuevo archivo Excel.

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Ordenar el DataFrame por la materia "Mat_EstructuraDatos" en orden ascendente
df_ordenado = df.sort_values(by='Mat_EstructuraDatos', ascending=True)

# Guardar el DataFrame ordenado en un nuevo archivo Excel
df_ordenado.to_excel('calificaciones_ordenadas.xlsx', index=False)

print("El archivo ha sido ordenado por 'Mat_EstructuraDatos' en orden ascendente y guardado como 'calificaciones_ordenadas.xlsx'")
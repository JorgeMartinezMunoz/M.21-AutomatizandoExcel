import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes, incrementa en 5
# el contenido de la materia "Mat_EstructuraDatos" para todos los registros y guarda el
# resultado en un nuevo archivo Excel.

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Incrementar en 5 el contenido de la materia "Mat_EstructuraDatos"
df['Mat_EstructuraDatos'] += 5

# Guardar el DataFrame modificado en un nuevo archivo Excel
df.to_excel('calificaciones_actualizadas.xlsx', index=False)

print("El contenido de la materia 'Mat_EstructuraDatos' ha sido incrementado en 5 para todos los registros y el resultado se ha guardado como 'calificaciones_actualizadas.xlsx'")
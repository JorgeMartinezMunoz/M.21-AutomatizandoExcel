import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes, filtra los estudiantes
# que tienen "Alberto" en el campo "NombreAlumno", muestra los apellidos de estos estudiantes,
# cuenta cuántos casos son y calcula el porcentaje respecto al total de registros.

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Filtrar los estudiantes que tienen "Alberto" en el campo "NombreAlumno"
estudiantes_alberto = df[df['NombreAlumno'].str.contains('Alberto', case=False, na=False)]

# Contar el número de estudiantes llamados "Alberto"
num_estudiantes_alberto = estudiantes_alberto.shape[0]

# Contar el número total de estudiantes
total_estudiantes = df.shape[0]

# Calcular el porcentaje de estudiantes llamados "Alberto"
porcentaje_alberto = (num_estudiantes_alberto / total_estudiantes) * 100

# Mostrar los valores de "ApellidoAlumno" de los estudiantes filtrados
apellidos_alberto = estudiantes_alberto['ApellidoAlumno']

# Imprimir los apellidos, el número de casos y el porcentaje
print("Los apellidos de los estudiantes llamados 'Alberto' son:")
print(apellidos_alberto)
print(f"El número de estudiantes llamados 'Alberto' es: {num_estudiantes_alberto}")
print(f"Esto representa el {porcentaje_alberto:.2f}% del total de estudiantes.")
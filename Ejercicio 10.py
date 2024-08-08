import pandas as pd

# Este programa lee un archivo Excel con calificaciones de estudiantes y muestra los apellidos
# de los estudiantes que tienen "Alberto" en el campo "NombreAlumno".

# Leer el archivo Excel
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Filtrar los estudiantes que tienen "Alberto" en el campo "NombreAlumno"
estudiantes_alberto = df[df['NombreAlumno'] == 'Alberto']

# Mostrar los valores de "ApellidoAlumno" de los estudiantes filtrados
apellidos_alberto = estudiantes_alberto['ApellidoAlumno']

# Imprimir los apellidos
print("Los apellidos de los estudiantes llamados 'Alberto' son:")
print(apellidos_alberto)
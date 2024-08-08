# Este programa lee un archivo de Excel llamado "calificaciones_alumnos.xlsx" que contiene
# las calificaciones de los alumnos en varias materias y genera un gráfico de barras para
# visualizar las calificaciones de cada alumno, asegurando que las etiquetas en el eje X
# no se encimen.

import pandas as pd
import matplotlib.pyplot as plt

try:
    # Leer el archivo de Excel y cargarlo en un DataFrame
    df = pd.read_excel('calificaciones_alumnos.xlsx', engine='openpyxl')

    # Verificar que el archivo contenga las columnas esperadas
    expected_columns = ['Nombre', 'Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']
    if not all(column in df.columns for column in expected_columns):
        raise ValueError(f"El archivo debe contener las siguientes columnas: {expected_columns}")

    # Configurar el tamaño de la figura para mejorar la visualización
    plt.figure(figsize=(12, 6))

    # Crear un gráfico de barras para cada columna de calificación
    for column in df.columns[1:]:  # Excluir la primera columna que es 'Nombre'
        plt.bar(df['Nombre'], df[column], label=column)

    # Configurar las etiquetas del eje X para que no se encimen
    plt.xticks(rotation=45, ha='right')

    # Añadir título y etiquetas de los ejes
    plt.title('Calificaciones de los alumnos')
    plt.xlabel('Alumnos')
    plt.ylabel('Calificaciones')

    # Añadir una leyenda para identificar cada materia
    plt.legend()

    # Ajustar el layout para que las etiquetas del eje X se vean completas
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

except FileNotFoundError:
    print("El archivo 'calificaciones_alumnos.xlsx' no se encuentra en el directorio actual.")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
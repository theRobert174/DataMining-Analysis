# Practica 4: Graficos
# Rodrigo Antonio Martinez Macias 1896222

import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from IPython.display import display
import numpy as np

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('Mexico_total_deceased.csv')

# Correcion de formato
# df['year'] = pd.to_datetime(df['year'], format='%Y-%m-%d', errors='coerce')

# Crear una figura y un eje para el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Definir los datos que se mostrarán en el gráfico
años = df['YEAR']  # Años en el eje X
poblacion_mujeres = df['FEMALE']
poblacion_hombres = df['MALE']

# Posición de las barras en el eje X
posicion_barras = range(len(años))

# Crear las barras para población masculina y femenina
barra_hombres = ax.bar(posicion_barras, poblacion_hombres, label='Hombres')
barra_mujeres = ax.bar(posicion_barras, poblacion_mujeres, label='Mujeres', alpha=0.7)

# Etiquetas, título y leyenda
ax.set_xlabel('Año')
ax.set_ylabel('Población')
ax.set_title('Numero de suicidios a lo largo de los años')
ax.set_xticks(posicion_barras)
ax.set_xticklabels(años, rotation=90)
ax.legend()

# Agregar etiquetas a las barras
for barra, poblacion in zip(barra_hombres, poblacion_hombres):
    ax.annotate(f'{poblacion}', xy=(barra.get_x() + barra.get_width() / 2, poblacion),
                xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', rotation=90)

for barra, poblacion in zip(barra_mujeres, poblacion_mujeres):
    ax.annotate(f'{poblacion}', xy=(barra.get_x() + barra.get_width() / 2, poblacion),
                xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', rotation=90)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
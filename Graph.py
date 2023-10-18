# Practica 4: Graficos
# Rodrigo Antonio Martinez Macias 1896222

import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from IPython.display import display
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('Mexico_total_deceased.csv')
cleanDF = pd.read_csv('Mexico_total_deceased.csv')
# Correcion de formato
# df['year'] = pd.to_datetime(df['year'], format='%Y-%m-%d', errors='coerce')


def deceased_through_years(): 
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


# deceased_through_years()

def range_between_79_00_deceased_women():
    # newDF = df['Anio'] >= 80's and <= 00
    results_by_year = df.groupby('YEAR')['MALE'].value_counts(normalize=True).unstack()

    print(results_by_year)#matrix

    # print("fffffffffffffffffffffffffffffffffffff")

    # range_deceased = df[df['MALE']>=500 and df['MALE']<=2000]
    # range_deceased = df[ df['MALE'] >= 500 or df['MALE'] <= 2000 ]
    range_deceased = df[ df['MALE'] >= 500 ]
    # print(range_deceased)#cantidad de cols y rows

    set_years = set(df['MALE'].unique())

    print(set_years)

    X = sm.add_constant(results_by_year.index)
    y = results_by_year[list(set_years)]

    # # print(X)
    # # print(y)

    model = sm.OLS(y, X).fit()

    print(model.summary())

    plt.scatter(X, y, label='Datos suicidios de hombres', color='blue')

    plt.plot(X, model.fittedvalues, label='Regresión lineal', color='red')

    plt.xlabel('Mes')
    plt.ylabel('Cantidad de suicidios')
    plt.legend()
    plt.title('Suicidio :D')
    plt.show()


range_between_79_00_deceased_women()
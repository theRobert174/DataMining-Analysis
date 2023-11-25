# Practica 3: Estadistica Desciptiva
# Rodrigo Antonio Martinez Macias 1896222

import pandas as pd
from tabulate import tabulate
from IPython.display import display

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('fixed_data_who_suicide.csv')

# Correcion de formato
df['year'] = pd.to_datetime(df['year'], format='%Y-%m-%d', errors='coerce')

# Utilizar la función unique() para obtener los países únicos y se transorma en un set
paises_unicos = set(df['country'].unique())

# Ordenar el conjunto alfabéticamente
paises_unicos = sorted(paises_unicos)



def Calculate_total_deceased_through_years(df: pd.DataFrame, country: str) -> pd.DataFrame:
    headers = ['YEAR','MALE','FEMALE','POPULATION']
    deceased_data = pd.DataFrame(columns=headers)

    # print( 'TOTAL DE REGISTROS:', df[ df['country'] == country].shape[0] )# total de registros

    # Se lee el pais especificado en los parametros
    country_data = df[ df['country'] == country]

    years_set = set(country_data['year'].unique())
    years_set = sorted(years_set)

    for year in years_set:

        # Se enfoca en la data de un unico anio
        year_data = country_data[ country_data['year'] == year ]

        # Se separan los datos de hombres y muejeres
        fem_data = year_data[ year_data['sex'] == 'female']
        male_data = year_data[ year_data['sex'] == 'male']

        # Se suman todas las muertes sin importar el rango de edad
        total_fem_deceased = fem_data['suicides_no'].sum()
        total_male_deceased = male_data['suicides_no'].sum()

        # Se suman todas las poblaciones de los rangos de edad de un anio en especifico
        total_population = year_data['population'].sum()

        # Se agrega una nueva fila al Dataframe con los datos de cada anio
        deceased_data.loc[len(deceased_data.index)] = [year.year, total_male_deceased, total_fem_deceased, total_population]

    display(deceased_data)

    # country_data.to_csv(f'{country}_total_deceased.csv', index=False)
    deceased_data.to_csv(f'{country}_total_deceased.csv', index=False)
    return deceased_data

Calculate_total_deceased_through_years(df, 'Mexico')
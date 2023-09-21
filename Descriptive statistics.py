# Practica 3: Estadistica Desciptiva
# Rodrigo Antonio Martinez Macias 1896222

import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('fixed_data_who_suicide.csv')

# Utilizar la función unique() para obtener los países únicos
paises_unicos = df['country'].unique()

# Convertir la lista de países únicos en un conjunto (set) si es necesario
paises_unicos_set = set(paises_unicos)

# Ordenar el conjunto alfabéticamente
paises_unicos_ordenados = sorted(paises_unicos_set)

# Imprimir los países únicos ordenados
# for pais in paises_unicos_ordenados:
#     print(pais)

def Calculate_total_deceased_through_years(df: pd.DataFrame, country: str):
    print( df[ df['country'] == country].shape[0] )# total de registros
    # print(paises_unicos)
    # print(paises_unicos_set)

    country_data = df[ df['country'] == country]

    years_set = set(country_data['year'].unique())

    # print(sorted(years_set))

    for year in sorted(years_set):
        year_data = country_data[ country_data['year'] == year ]
        # print(year_data, 'FIN')

        fem_data = year_data[ year_data['sex'] == 'female']
        male_data = year_data[ year_data['sex'] == 'male']

        total_fem = fem_data['suicides_no'].sum()
        total_male = male_data['suicides_no'].sum()

        print({f'DATE: {year}, FEMALE: {total_fem}, MALE: {total_male}'})




    country_data.to_csv(f'{country}_total_deceased.csv', index=False)

Calculate_total_deceased_through_years(df, 'Mexico')
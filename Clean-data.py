# Practica 2: Limpieza de datos
# Rodrigo Antonio Martinez Macias 1896222

import pandas as pd

df = pd.read_csv('who_suicide_statistics.csv')

# Da formato de datetime a los anios
df['year'] = pd.to_datetime(df['year'], format='%Y')

# Se define un rango para mas de 75 anios
df['age'] = df['age'].str.replace('75+', '75-100')

# Se separa los limites de las edades en dos columnas
df[['init_age', 'last_age']] = df['age'].str.split('-', expand=True)

# Se remueve la palabra years de las columnas
df['init_age'] = df['init_age'].str.replace(' years', '')
df['last_age'] = df['last_age'].str.replace(' years', '')


# Se elimina la vieja columna de anios
df = df.drop(columns=['age'])

# Los datos nulos se llenan con ceros
df = df.fillna('0')

# Se definen los tipos de datos
df['init_age'] = df['init_age'].astype(int)
df['last_age'] = df['last_age'].astype(int)
df['suicides_no'] = df['suicides_no'].astype(int)
df['population'] = df['population'].astype(int)

# Se reorganizan las columnas 
df = df[['country','year','sex','init_age','last_age','suicides_no','population']]

# Se genera un nuevo csv con los nuevos datos limpios
df.to_csv('fixed_data_who_suicide.csv', index=False)

# Area de pruebas
# print(df.head())
# print('---------------')
# print(df.info())
# print('---------------')
# print(df.describe())
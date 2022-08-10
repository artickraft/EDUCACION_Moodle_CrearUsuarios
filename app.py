import pandas as pd
from unidecode import unidecode

archivo = input('Mete tu archivo CSV: ')
archivo = archivo.replace('"', '')
df = pd.read_csv(archivo, sep=';')

nombre_util = df['firstname'].str.lower().str.split(' ').str[0].apply(unidecode)

# df['firstname'] = df['firstname'].str.lower()
# df['firstname'] = df['firstname'].str.split(' ').str[0].apply(unidecode)

apellido_util = df['lastname'].str.lower().str.split(' ').str[0].apply(unidecode)

# df['lastname'] = df['lastname'].str.lower()
# df['lastname'] = df['lastname'].str.split(' ').str[0].apply(unidecode)

df['username'] = nombre_util + '.' + apellido_util


print(df)
df.to_csv('Usuarios_Final.csv', index=False, sep=';')

import pandas as pd
from unidecode import unidecode
import streamlit as st

st.set_page_config(
    page_title="APP Generar Usernames",
    page_icon="💼",
)

st.title('📋 Generar *usernames*')
st.caption('Sube un archivo CSV con las columnas [username,firstname,lastname,email,password,course1,type1] y el programa te devolverá el mismo CSV pero con la columna username rellenada usando la primera palabra del firstname y del lastname unidas por un . y en minúsculas sin caracteres especiales.')

archivo = st.file_uploader("Sube tu CSV", accept_multiple_files=False) # input('Mete tu archivo CSV: ')
# archivo = archivo.replace('"', '')
if archivo is not None:
    df = pd.read_csv(archivo, sep=';')

    nombre_util = df['firstname'].str.lower().str.split(' ').str[0].apply(unidecode)
    apellido_util = df['lastname'].str.lower().str.split(' ').str[0].apply(unidecode)

    df['username'] = nombre_util + '.' + apellido_util

    @st.cache
    def convert_df(df):
        return df.to_csv(index=False, sep=';')

    csv = convert_df(df)
    st.dataframe(df)
    st.download_button(label='Descargar CSV', data=csv, mime='text/csv')

st.caption('Hecho por Nil Civis para © 2022 LETCRAFT DESARROLLOS AUDIOVISUALES, SOCIEDAD LIMITADA. ALL RIGHTS RESERVED')
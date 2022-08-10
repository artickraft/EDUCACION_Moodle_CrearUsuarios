import pandas as pd
from unidecode import unidecode
import streamlit as st



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


import streamlit as st
import pandas as pd

st.title("Copa do Mundo Futebol - FIFA")

copas = pd.read_csv('WorldCups.csv')
copas['Year'] = copas['Year'].astype(str)
copas['Year_Country'] = copas['Year']+" - "+copas['Country']

st.sidebar.header("FILTROS")
list_year_country = []
list_year_country = copas['Year_Country'].values.tolist()
selected_copa = st.sidebar.selectbox('Selecione a Copa',list_year_country)


df_copas = copas.loc[copas['Year_Country'] == selected_copa]
df_copas = df_copas.set_index('Year_Country')
st.subheader("Copa de " + selected_copa)
st.dataframe(df_copas)


campeao = copas.loc[copas['Winner'] == df_copas['Winner'].values]
st.subheader("CAMPEÃO: " + campeao)

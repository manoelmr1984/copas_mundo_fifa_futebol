import streamlit as st
import pandas as pd

st.title("Copa do Mundo Futebol - FIFA")

copas = pd.read_csv('WorldCups.csv')
copas['Year'] = copas['Year'].astype(str)
copas['Year_Country'] = copas['Year']+" - "+copas['Country']

st.sidebar.header("Selecione a Copa")
list_year_country = []
list_year_country = copas['Year_Country'].values.tolist()
selected_copa = st.sidebar.selectbox('',list_year_country)

def load_copa(year_country):   
  year_country = selected_copa
  return copas.loc[copas['Year_Country'] == year_country]

df_copas = load_copa(selected_copa)
df_copas = df_copas.set_index('Year_Country')
st.subheader("Copa de " + selected_copa)
st.dataframe(df_copas)

#list_campeoes = []
#list_campeoes = df_copas['Winner'].values.tolist()
campeao = df_copas['Winner'].Text
st.subheader(campeao)

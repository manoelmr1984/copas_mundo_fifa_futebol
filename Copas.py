import streamlit as st
import pandas as pd

st.title("Copa do Mundo Futebol - FIFA")

copas = pd.read_csv('WorldCups.csv')
copas['Year'] = copas['Year'].astype(str)
copas['Year_Country'] = copas['Year']+" - "+copas['Country']

st.sidebar.header("Selecione a Copa")
list_copa = []
list_copa = copas['Year_Country'].values.tolist()
selected_copa = st.sidebar.selectbox('',list_copa)

def load_data(ano_anfitriao):   
  ano_anfitriao = selected_copa
  return copas.loc[copas['Year_Country'] == ano_anfitriao]

df_copas = load_data(selected_copa)
df_copas = df_copas.set_index('Year_Country')
st.subheader("Copa de "+selected_copa)
st.dataframe(df_copas)

#list_campeoes = []
#list_campeoes = df_copas['Winner'].values.tolist()
list_campeoes = df_copas['Winner']
st.subheader(list_campeoes)

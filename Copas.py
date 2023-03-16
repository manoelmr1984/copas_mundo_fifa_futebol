import streamlit as st
import pandas as pd

st.title("Copa do Mundo Futebol - FIFA")

copas = pd.read_csv('WorldCups.csv')
copas['Year'] = copas['Year'].astype(str)
copas['Year_Country'] = copas['Year']+" - "+copas['Country']

st.sidebar.header("Selecione a Copa")
list_copa=[]
list_copa=copas['Year_Country'].values.tolist()
selected_copa = st.sidebar.selectbox('',list_copa)

def load_data(ano_anfitriao):   
  ano_anfitriao = selected_copa
  return copas.loc[copas['Year_Country']==ano_anfitriao]

df = load_data(selected_copa)
df = df.set_index('Year_Country')
st.subheader("Copa de "+selected_copa)
st.dataframe(df)

def load_campeao(campeao):   
  campeao = selected_copa
  return copas.loc[copas['Winner']==campeao]

df = load_campeao(selected_copa)
st.subheader(campeao)

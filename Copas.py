import streamlit as st
import pandas as pd

st.title("Copa do Mundo Futebol - FIFA")

copas = pd.read_csv('WorldCups.csv')
copas['Year'] = copas['Year'].astype(str)
copas['Year_Country'] = copas['Year']+" - "+copas['Country']

st.sidebar.header("Ano Copa")
list_copa=[]
list_copa=copas['Year_Country'].values.tolist()
selected_copa = st.sidebar.selectbox('Season',list_copa)

def load_data(season):   
  season = selected_copa
  return copas.loc[copas['Year_Country']==season]

df = load_data(selected_copa)
df=df.set_index('Year_Country')
st.subheader("Copa de "+selected_copa)
st.dataframe(df)

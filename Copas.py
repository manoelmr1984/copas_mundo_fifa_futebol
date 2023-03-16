import streamlit as st
import pandas as pd
#import numpy as np
#import base64

st.title("Copa do Mundo Futebol - FIFA")

copas = pd.read_csv('WorldCups.csv')
copas['Year'] = copas['Year'].astype(str)

st.sidebar.header("Ano Copa")
list_ano=[]
list_ano=copas['Year'].values.tolist()
selected_season = st.sidebar.selectbox('Season',list_ano)

def load_data(season):   
  season = selected_season
  #return copas
  return copas.loc[copas['Year']==season]

df = load_data(selected_season)

st.subheader("Copa de "+selected_season)
st.dataframe(df)

campeao = df['Winner']

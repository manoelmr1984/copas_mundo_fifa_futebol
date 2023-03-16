import streamlit as st
import pandas as pd
#import numpy as np
#import base64

st.title("Copa do Mundo Futebol - FIFA")

copas = pd.read_csv('WorldCups.csv')

st.sidebar.header("Ano Copa")
list_ano=[]
list_ano=copas['Year'].values.tolist()
selected_season = st.sidebar.selectbox('Season',list_ano)

def load_data(season):   
  if selected_season == 1930:
    season = 1930
  if selected_season == 1950:
    season = 1950
  if selected_season == 2014:
    season = 2014
    
  data = pd.read_csv('WorldCups.csv')
  return data

df = load_data(selected_season)

st.subheader("por manoelmr")
st.dataframe(df)

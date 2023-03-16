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

#def load_copa(year_country):
#  year_country = selected_copa
#  return copas.loc[copas['Year_Country'] == year_country]

#df_copas = load_copa(selected_copa)
#df_copas = df_copas.set_index('Year_Country')
#st.subheader("Copa de " + selected_copa)
#st.dataframe(df_copas)


df_campeao = copas.loc[copas['Year_Country'] == selected_copa]
#df_copas = load_copa(selected_copa)
df_campeao = df_campeao.set_index('Year_Country')
st.subheader("Copa de " + df_campeao['Winner'])
st.dataframe(df_campeao)

#list_campeoes = []
#list_campeoes = df_copas['Winner'].values.tolist()
#campeao = df_copas['Winner'].values
#st.subheader(campeao)



#def load_campeao(campeao): 
#  campeao = selected_copa[0]
#  return copas.loc[copas['Winner'] == campeao]

#df_campeao = load_campeao(selected_copa)
#df_campeao = df_campeao.set_index('Winner')
#st.subheader("CAMPEÃO:  " + selected_copa)
#st.dataframe(df_campeao)

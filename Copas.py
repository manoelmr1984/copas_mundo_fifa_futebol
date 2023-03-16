import streamlit as st
import pandas as pd

st.title("Copa do Mundo Futebol - FIFA")

copas = pd.read_csv('WorldCups.csv')
copas['Year'] = copas['Year'].astype(str)
copas['Year_Country'] = copas['Year']+" - "+copas['Country']

st.sidebar.header("Selecione a Copa")
list_year_country = []
list_year_country = copas['Year_Country'].values.tolist()
selected_copa = st.sidebar.selectbox(list_year_country)


df_campeao = copas.loc[copas['Year_Country'] == selected_copa]
#df_copas = load_copa(selected_copa)
df_campeao = df_campeao.set_index('Year_Country')
st.subheader("Copa de " + selected_copa)
st.dataframe(df_campeao)



st.subheader("CAMPEÃO: " + df_campeao['Winner'])

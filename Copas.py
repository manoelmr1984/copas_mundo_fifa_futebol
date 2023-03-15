import streamlit as st
import pandas as pd
import numpy as np
import base64

st.title("Copa do Mundo Futebol - FIFA")

st.sidebar.header("País Sede")

copas = pd.read_csv('WorldCups.csv')
list_campeoes=[]
list_campeoes=copas['Country'].values.tolist()
selected_league = st.sidebar.selectbox('League',list_campeoes)
#selected_league = st.sidebar.selectbox('League',['Uruguay','England','Germany','Italy','Spain','France'])

st.sidebar.header("Ano Copa")
selected_season = st.sidebar.selectbox('Season', ['2021/2022','2020/2021','2019/2020'])

# WebScraping Football Data
def load_data(league, season):
#def load_data(league):
  
  if selected_league == 'Uruguay':
    league = 'E0'
  if selected_league == 'England':
    league = 'E0'
  if selected_league == 'Germany':
    league = 'D1'
  if selected_league == 'Italy':
    league = 'I1'
  if selected_league == 'Spain':
    league = 'SP1'
  if selected_league == 'France':
    league = 'F1'
   
  if selected_season == '2021/2022':
    season = '2122'
  if selected_season == '2020/2021':
    season = '2021'
  if selected_season == '2019/2020':
    season = '1920'
    
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  #data = pd.read_csv(copas)
  return data

df = load_data(selected_league, selected_season)
#df = load_data(selected_league)

st.subheader("Dataframe: "+selected_league)
st.dataframe(df)

#def filedownload(df):
#    csv = df.to_csv(index=False)
#    b64 = base64.b64encode(csv.encode()).decode()
#    href = f'<a href="data:file/csv;base64,{b64}" download="Base_de_Dados.csv">Download CSV File</a>'
#    return href

#st.markdown(filedownload(df), unsafe_allow_html=True)

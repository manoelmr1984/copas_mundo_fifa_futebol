import streamlit as st
import pandas as pd
import numpy as np
import base64

st.title("Copa do Mundo Futebol - FIFA")

copas = pd.read_csv('WorldCups.csv')

##st.sidebar.header("País Sede")
##list_campeoes=[]
##list_campeoes=copas['Country'].values.tolist()
##selected_league = st.sidebar.selectbox('League',list_campeoes)
#selected_league = st.sidebar.selectbox('League',['Uruguay','England','Germany','Italy','Spain','France'])

st.sidebar.header("Ano Copa")
list_ano=[]
list_ano=copas['Year'].values.tolist()
selected_season = st.sidebar.selectbox('Season',list_ano)
#selected_season = st.sidebar.selectbox('Season', ['2021/2022','2020/2021','2019/2020'])

# WebScraping Football Data
#def load_data(league, season):
def load_data(season):
  
  #if selected_league == 'Uruguay':
  #  league = 'E0'
  #if selected_league == 'England':
  #  league = 'E0'
  #if selected_league == 'Germany':
  #  league = 'D1'
  #if selected_league == 'Italy':
  #  league = 'I1'
  #if selected_league == 'Spain':
  #  league = 'SP1'
  #if selected_league == 'France':
  #  league = 'F1'
   
  if selected_season == 1930:
    #season = '2223'
    season = 1930
  if selected_season == 1950:
    #season = '2021'
    season = 1950
  if selected_season == 2014:
    #season = '1920'
    season = 2014
    
  ##url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  #url = "https://www.football-data.co.uk/mmz4281/"+season+"/D1.csv"
  url = pd.read_csv('WorldCups.csv')
  data = pd.read_csv(url)
  return data

#df = load_data(selected_league, selected_season)
df = load_data(selected_season)

#st.subheader("Dataframe: "+selected_league)
st.subheader("por manoelmr")
st.dataframe(df)

#def filedownload(df):
#    csv = df.to_csv(index=False)
#    b64 = base64.b64encode(csv.encode()).decode()
#    href = f'<a href="data:file/csv;base64,{b64}" download="Base_de_Dados.csv">Download CSV File</a>'
#    return href

#st.markdown(filedownload(df), unsafe_allow_html=True)

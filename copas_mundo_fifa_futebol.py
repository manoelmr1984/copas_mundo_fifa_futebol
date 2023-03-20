#importando bibliotecas
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
from PIL import Image


#carregando os dados
copas = pd.read_excel('bd.xlsx',sheet_name='copas')
partidas = pd.read_excel('bd.xlsx',sheet_name='partidas')

#converte a colunas em string
copas['ano_copa'] = copas['ano_copa'].astype(str)
partidas['ano_copa'] = partidas['ano_copa'].astype(str)
partidas['id_partida'] = partidas['id_partida'].astype(str)

#insere a coluna "ano_copa_sede" concatenando "ano_copa" + "sede"
copas['ano_copa_sede'] = copas['ano_copa']+" - "+copas['sede']

#insere a coluna de média gols por partidas na copa
copas['gols_partida'] = copas['gols_marcados_copa'] / copas['quant_partidas_copa']

#convertendo a coluna "publico_copa" em inteiro
copas['publico_copa'] = copas['publico_copa'].apply(lambda x: str(x).replace(".",""))
copas['publico_copa'] = copas['publico_copa'].astype('int64')

#cria uma lista para listbox
list_ano_copa_sede = []
list_ano_copa_sede = copas['ano_copa_sede'].values.tolist()
list_ano_copa_sede = sorted(list_ano_copa_sede, reverse=True) #ordena a lista do maior para o menor
selected_copa = st.sidebar.selectbox('Selecione uma copa abaixo:',list_ano_copa_sede)


#cria uma dataframe da copa selecionada
filtra_copa = copas.loc[copas['ano_copa_sede'] == selected_copa]
logo_copa = filtra_copa.iloc[0]['img_logo']

#inserindo o título da página
titulo_copa = filtra_copa.iloc[0]['desc_copa']
img_copa = filtra_copa.iloc[0]['img_logo']
#col_taca, col_titulo = st.columns([10,150])
#with col_taca:
st.sidebar.image(img_copa, width = 210)

#with col_titulo:
st.title(titulo_copa)


#INSERINDO INFORMAÇÕES DA COPA FILTRADA
col_campeao, col_vice, col_terceiro, col_quarto = st.columns(4)
with col_campeao:
    st.text('CAMPEÃO:')
    nome_pais = filtra_copa.iloc[0]['campeao']
    img_pais = filtra_copa.iloc[0]['img_campeao']
    st.image(img_pais,
                width = 100,
                caption = nome_pais
                )

with col_vice:
    st.text('VICE-CAMPEÃO:')
    nome_pais = filtra_copa.iloc[0]['2nd']
    img_pais = filtra_copa.iloc[0]['img_2nd']
    st.image(img_pais,
                width = 100,
                caption = nome_pais
                )

with col_terceiro:
    st.text('3º COLOCADO:')
    nome_pais = filtra_copa.iloc[0]['3nd']
    img_pais = filtra_copa.iloc[0]['img_3nd']
    st.image(img_pais,
                width = 100,
                caption = nome_pais
                )

with col_quarto:
    st.text('4º COLOCADO:')
    nome_pais = filtra_copa.iloc[0]['4nd']
    img_pais = filtra_copa.iloc[0]['img_4nd']
    st.image(img_pais,
                width = 100,
                caption = nome_pais
                )


#informações da copa selecionada
st.subheader('INFORMAÇÕES DA COPA')
col_gols, col_partidas, col_equipes, col_publico = st.columns(4)
gols_total = filtra_copa.iloc[0]['gols_marcados_copa']
partidas_total = filtra_copa.iloc[0]['quant_partidas_copa']
equipes_total = filtra_copa.iloc[0]['quant_participantes_copa']
publico_total = filtra_copa.iloc[0]['publico_copa']

with col_gols:
    st.text('GOLS MARCADOS: ' + str(gols_total))

with col_partidas: 
    st.text('PARTIDAS: ' + str(partidas_total))

with col_equipes:
    st.text('PARTICIPANTES: '+ str(equipes_total))

with col_publico:
    st.text('PÚBLICO: ' + str(publico_total))


st.markdown('---')
st.subheader('TABELA DE JOGOS')


#tabela de jogos
partidas = partidas.loc[partidas['ano_copa'] == filtra_copa.iloc[0]['ano_copa']]
partidas = partidas[['ano_copa', 'data_hora', 'id_fase', 'fase_grupo', 'time1', 'gols_time1', 
                     'placar', 'gols_time2', 'time2', 'win_conditions']]

#cria uma listbox com as fases da copa selecionada
filtra_fases_partidas = partidas.loc[partidas['ano_copa'] == filtra_copa.iloc[0]['ano_copa']]

filtra_fases_partidas = filtra_fases_partidas.groupby(by=['id_fase', 'fase_grupo']).sum()[['gols_time1']]
filtra_fases_partidas = filtra_fases_partidas.rename(columns={'gols_time1': 'Titulos'})
filtra_fases_partidas = filtra_fases_partidas.reset_index()

#st.dataframe(filtra_fases_partidas)
list_fases = []
list_fases = filtra_fases_partidas['fase_grupo'].values.tolist()
selected_fase = st.selectbox('Selecione uma fase abaixo:', list_fases)

#tabela de jogos
partidas = partidas.loc[partidas['fase_grupo'] == selected_fase]
partidas = partidas[['data_hora', 'time1', 'placar', 'time2', 'win_conditions']]
partidas = partidas.set_index('data_hora')

st.dataframe(partidas)
st.markdown("---")


instagram, facebook, linked, twitter, gmail = st.columns(5)
with instagram:
    logo = 'https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg'
    url = "https://www.instagram.com/marques_manoel"
    st.markdown(f'''<p> <a href="{url}"><img src="{logo}" widht="30" height="30"></p''', unsafe_allow_html=True)

with facebook:
    logo = 'https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Facebook_f_logo_%282021%29.svg/2048px-Facebook_f_logo_%282021%29.svg.png'
    url = 'https://www.facebook.com/manoelmr1984?mibextid=ZbWKwL'
    st.markdown(f'''<p> <a href="{url}"><img src="{logo}" widht="30" height="30"></p''', unsafe_allow_html=True)

with linked:
    logo = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/LinkedIn_icon_circle.svg/800px-LinkedIn_icon_circle.svg.png'
    url = 'https://www.linkedin.com/in/manoel-marques-ribeiro-6b726564'
    st.markdown(f'''<p> <a href="{url}"><img src="{logo}" widht="30" height="30"></p''', unsafe_allow_html=True)

with twitter:
    logo = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Twitter-logo.svg/2491px-Twitter-logo.svg.png'
    url = 'https://twitter.com/ManoelM53217392?t=TWNj7wMhE0BKbGJLarNowg&s=03'
    st.markdown(f'''<p> <a href="{url}"><img src="{logo}" widht="30" height="30"></p''', unsafe_allow_html=True)

with gmail:
    logo = 'https://www.vectorlogo.zone/logos/gmail/gmail-ar21.png'
    url = 'manoelmr1984@gmail.com'
    st.markdown(f'''<p> <a href="{url}"><img src="{logo}" widht="30" height="30"></p''', unsafe_allow_html=True)

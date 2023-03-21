#importando bibliotecas
import streamlit as st
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#import plotly.express as px
#from PIL import Image


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
st.sidebar.image(img_copa, width = 210)
#st.header(titulo_copa)

tab1, tab2, tab3 = st.tabs(['RESUMO COPA', 'TABELA DE JOGOS', 'HISTÓRICO'])
with tab1:
    st.markdown('**TOP 4**')
    #INSERINDO INFORMAÇÕES DA COPA FILTRADA
    col_campeao, col_vice, col_terceiro, col_quarto = st.columns(4)  
    with col_campeao:
        st.markdown('_campeão:_')
        nome_pais = filtra_copa.iloc[0]['campeao']
        img_pais = filtra_copa.iloc[0]['img_campeao']
        st.image(img_pais,
                    width = 100,
                    caption = nome_pais
                    )

    with col_vice:
        st.markdown('_vice-campeão:_')
        nome_pais = filtra_copa.iloc[0]['2nd']
        img_pais = filtra_copa.iloc[0]['img_2nd']
        st.image(img_pais,
                    width = 100,
                    caption = nome_pais
                    )

    with col_terceiro:
        st.markdown('_3º colocado:_')
        nome_pais = filtra_copa.iloc[0]['3nd']
        img_pais = filtra_copa.iloc[0]['img_3nd']
        st.image(img_pais,
                    width = 100,
                    caption = nome_pais
                    )

    with col_quarto:
        st.markdown('_4º colocado:_')
        nome_pais = filtra_copa.iloc[0]['4nd']
        img_pais = filtra_copa.iloc[0]['img_4nd']
        st.image(img_pais,
                    width = 100,
                    caption = nome_pais
                    )

    #informações da copa selecionada
    st.markdown('**INFORMAÇÕES DA COPA**')
    col_gols, col_partidas, col_equipes, col_publico = st.columns(4)
    gols_total = filtra_copa.iloc[0]['gols_marcados_copa']
    partidas_total = filtra_copa.iloc[0]['quant_partidas_copa']
    equipes_total = filtra_copa.iloc[0]['quant_participantes_copa']
    publico_total = filtra_copa.iloc[0]['publico_copa']

    with col_gols:
        st.text(str(gols_total) + ' gols')

    with col_partidas: 
        st.text(str(partidas_total) + ' partidas')

    with col_equipes:
        st.text(str(equipes_total) + ' equipes')

    with col_publico:
        st.text(str(publico_total) + ' público')

with tab2:
    #tabela de jogos filtrando a copa selecionada
    st.markdown('**TABELA DE JOGOS**')
    partidas = partidas.loc[partidas['ano_copa'] == filtra_copa.iloc[0]['ano_copa']]
    partidas['ref_fase_grupo'] = partidas['tipo_fase'] + " - " + partidas['fase_grupo']
    partidas = partidas[['ano_copa', 'data_hora', 'id_fase', 'fase_grupo', 'tipo_fase', 'time1', 
                        'gols_time1', 'placar', 'gols_time2', 'time2', 'win_conditions', 'ref_fase_grupo', 'img_time1', 'img_time2']]

    tipo_fase, mata_mata, em_branco = st.columns([2,2,3])
    with tipo_fase:
        list_tipo_fase = []
        list_tipo_fase = partidas['tipo_fase'].values.tolist()
        list_tipo_fase = list(dict.fromkeys(list_tipo_fase))
        selecao_tipo_fase = st.selectbox('Selecione uma fase abaixo:', list_tipo_fase)

        filtra_fase_grupo = partidas.loc[partidas['tipo_fase'] == selecao_tipo_fase]

    with mata_mata:
        list_fase_grupo = []
        list_fase_grupo = filtra_fase_grupo['fase_grupo'].values.tolist()
        list_fase_grupo = list(dict.fromkeys(list_fase_grupo))
        selecao_fase_grupo = st.selectbox('', list_fase_grupo)

    with em_branco:
        st.text('')

    ref_filtra_fase = selecao_tipo_fase + ' - ' + selecao_fase_grupo

    #tabela de jogos
    partidas = partidas.loc[partidas['ref_fase_grupo'] == ref_filtra_fase]
    partidas = partidas[['data_hora', 'time1', 'img_time1', 'placar', 'img_time2', 'time2']]

    #renomeando as colunas
    partidas = partidas.rename(columns={'data_hora': 'DATA HORA', 'time1': 'MANDANTE', 'placar': 'x', 
                                        'time2': 'VISITANTE', 'img_time1': 'img', 'img_time2': 'img'})
    #partidas = partidas.set_index('DATA HORA')

    def path_to_image_html(path):
        return '<img src="' + path + '" width="30" >'

    st.markdown(
        partidas.to_html(escape=False, formatters=dict(img=path_to_image_html)),
        unsafe_allow_html=True,
    )

with tab3:
    st.markdown('**OS CAMPEÕES**')
    #campeões
    copas = copas.rename(columns={'campeao': 'PAÍS CAMPEÃO', 'img_campeao': 'BANDEIRA'})
    campeoes = copas.groupby(by=['PAÍS CAMPEÃO','BANDEIRA']).sum()[['Conta']]
    campeoes = campeoes.rename(columns={'Conta': 'TÍTULOS'})
    campeoes = campeoes.reset_index()

    def path_to_image_html(path):
        return '<img src="' + path + '" width="50" >'
    
    st.markdown(
        campeoes.to_html(escape=False, formatters=dict(BANDEIRA=path_to_image_html)),
        unsafe_allow_html=True,
    )
    
    st.markdown('---')
    st.markdown('**EVOLUÇÃO DAS COPAS EM NÚMEROS**')
    ###########################################################################
    select_opcao = st.selectbox('Selecione uma copa abaixo:', ['Gol Marcados', 'Média Gols', 'Partidas', 'Participantes', 'Público'])

    if select_opcao == 'Gol Marcados':
        valores = copas['gols_marcados_copa']
        titulo_grafico = 'GOLS MARCADOS por COPA'
    elif select_opcao == 'Média Gols':
        valores = copas['gols_partida']
        titulo_grafico = 'MÉDIA DE GOLS/PARTIDA por COPA'
    elif select_opcao == 'Partidas':
        valores = copas['quant_partidas_copa']
        titulo_grafico = 'QUANTIDADE DE PARTIDAS por COPA'
    elif select_opcao == 'Participantes':
        valores = copas['quant_participantes_copa']
        titulo_grafico = 'QUANTIDADE DE PARTICIPANTES por COPA'
    elif select_opcao == 'Público':
        valores = copas['publico_copa']
        titulo_grafico = 'PÚBLICO PRESENTE por COPA'
    ###########################################################################

    label = copas['ano_copa']

    plt.figure(figsize=(8, 4))
    plt.style.use('ggplot')
    plt.tight_layout()
    plt.title(titulo_grafico, fontsize=10, fontweight='bold', fontstyle='italic', fontfamily='trebuchet ms')
    plt.xticks(rotation=90, fontsize=6)
    plt.yticks(fontsize=6)
    plt.xlabel(label.name, fontsize=5)
    plt.ylabel(valores.name, fontsize=5)

    plt.plot(label, valores, linewidth='8', color='red', alpha=0.15)

    plt.plot(label,valores,
             color='red',
             linewidth='1',
             #linestyle='--',
             marker='o',
             markersize=4,
             mfc='white',
             mec='red')
    plt.grid(axis='x', linewidth='0.5')
    plt.grid(axis='y', linewidth='0.5')

    for (i, valor) in enumerate(valores, start=0):
        plt.text(x=label[i],
                 y=valor * 1.02,
                 s=f'{valor}',
                 ha='center',
                 fontsize=8,
                 color='blue',
                 fontstyle='italic')
    st.pyplot(plt)


st.markdown("---")
#rodapé da página
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

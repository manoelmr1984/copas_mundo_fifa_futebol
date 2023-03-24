#importando bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px


#carregando os dados
copas = pd.read_csv('Copas.csv')
partidas = pd.read_csv('Partidas.csv')


#converte colunas em string
copas['ano_copa'] = copas['ano_copa'].astype(str)
partidas['ano_copa'] = partidas['ano_copa'].astype(str)
partidas['id_partida'] = partidas['id_partida'].astype(str)
partidas['fase_grupo'] = partidas['fase_grupo'].astype(str)

#insere a coluna "ano_copa_sede" concatenando "ano_copa" + "sede"
copas['ano_copa_sede'] = copas['ano_copa']+" - "+copas['sede']

#insere a coluna de média gols por partidas na copa
copas['gols_partida'] = copas['gols_marcados_copa'] / copas['quant_partidas_copa']

#insere coluna de total de gols da partida
partidas['gols_na_partida'] = partidas['gols_time1'] + partidas['gols_time2']

#convertendo a coluna "publico_copa" em inteiro
copas['publico_copa'] = copas['publico_copa'].apply(lambda x: str(x).replace(".",""))
copas['publico_copa'] = copas['publico_copa'].astype('int64')

#partidas['placar'] = partidas['placar'].replace('-','x')

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

tab1, tab2, tab3 = st.tabs(['RESUMO COPA', 'TABELA DE JOGOS', 'HISTÓRICO COPAS'])
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

    partidas = partidas.loc[partidas['ano_copa'] == filtra_copa.iloc[0]['ano_copa']]

    #gera gráfico gols partidas fase
    graf_gol_partida_fase = px.box(partidas, 
                                   x='fase_grupo', 
                                   y=['gols_na_partida'], 
                                   title='GOLS MARCADOS por FASE', 
                                   points='all')
    
    #plota gráfico gols partidas fase
    st.plotly_chart(graf_gol_partida_fase)
with tab2:
    #tabela de jogos filtrando a copa selecionada
    st.markdown('**TABELA DE JOGOS**')

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

    campeoes = copas.groupby(by=['campeao','img_campeao']).sum()[['Conta']]
    campeoes = campeoes.rename(columns={'Conta': 'titulos'})
    campeoes = campeoes.reset_index()

    listagem = []
    lista = []
    lista_campeoes = campeoes['campeao'].values.tolist()

    for campeao in lista_campeoes:
        listagem_ano = []
        for x in range(len(copas)):
            i = copas['campeao'][x]
            ano = copas['ano_copa'][x]
            if i == campeao:
                listagem_ano.append(ano)
                listagem.append([campeao, copas['img_campeao'][x], len(listagem_ano), listagem_ano])

        registro = len(listagem)-1
        lista.append(listagem[registro])

    #criando a tabela
    resumo_campeoes = pd.DataFrame(lista, columns = ['PAÍSES CAMPEÕES', 'BANDEIRA', '🏆', 'LISTA DE ANO DAS CONQUISTAS'])#TÍTULOS

    resumo_campeoes['LISTA DE ANO DAS CONQUISTAS'] = resumo_campeoes['LISTA DE ANO DAS CONQUISTAS'].apply(lambda x: str(x).replace("[",""))
    resumo_campeoes['LISTA DE ANO DAS CONQUISTAS'] = resumo_campeoes['LISTA DE ANO DAS CONQUISTAS'].apply(lambda x: str(x).replace("]",""))
    resumo_campeoes['LISTA DE ANO DAS CONQUISTAS'] = resumo_campeoes['LISTA DE ANO DAS CONQUISTAS'].apply(lambda x: str(x).replace("'",""))
    resumo_campeoes['LISTA DE ANO DAS CONQUISTAS'] = resumo_campeoes['LISTA DE ANO DAS CONQUISTAS'].apply(lambda x: str(x).replace(","," |"))

    def path_to_image_html(path):
        return '<img src="' + path + '" width="40" >'
    
    st.markdown(
        resumo_campeoes.to_html(escape=False, formatters=dict(BANDEIRA=path_to_image_html)),
        unsafe_allow_html=True,
    )

    graf_gols_campeao = px.box(copas, x='campeao', 
                               y='gols_marcados_copa', 
                               title='CORRELAÇÃO ENTRE CAMPEÕES x GOLS MARCADOS NAS COPAS CONQUISTADAS', 
                               points='all')
    st.plotly_chart(graf_gols_campeao)

    st.markdown('---')
    st.markdown('**EVOLUÇÃO DAS COPAS EM NÚMEROS**')
    select_opcao = st.selectbox('Selecione uma copa abaixo:', ['Gol Marcados', 'Média Gols', 'Partidas', 'Participantes', 'Público'])

    if select_opcao == 'Gol Marcados':
        evolucao_copas = (copas.groupby(by=['ano_copa']).sum()[['gols_marcados_copa']])
    elif select_opcao == 'Média Gols':
        evolucao_copas = (copas.groupby(by=['ano_copa']).sum()[['gols_partida']])
    elif select_opcao == 'Partidas':
        evolucao_copas = (copas.groupby(by=['ano_copa']).sum()[['quant_partidas_copa']])
    elif select_opcao == 'Participantes':
        evolucao_copas = (copas.groupby(by=['ano_copa']).sum()[['quant_participantes_copa']])
    elif select_opcao == 'Público':
        evolucao_copas = (copas.groupby(by=['ano_copa']).sum()[['publico_copa']])

    st.line_chart(evolucao_copas, height=300)



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
    logo = 'https://1drv.ms/i/s!AhTpg3jKD9Je7EGg7KPe8yhpJTmA?e=6NIjbc'
    url = 'manoelmr1984@gmail.com'
    st.markdown(f'''<p> <a href="{url}"><img src="{logo}" widht="30" height="30"></p''', unsafe_allow_html=True)

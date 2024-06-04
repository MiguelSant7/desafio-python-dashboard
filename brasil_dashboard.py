### Importação de Bibliotecas Streamlit, Pandas, Plotly(express/graph_objs)
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

## Configurações Iniciais do Dashboard
st.set_page_config(
    page_title="Índices brasileiros",
    page_icon="🇧🇷",
    layout="wide",
    initial_sidebar_state="expanded",
)

## Importação de arquivo CSS(style.css)
def local_css(file_name):
   with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")


## Carregamento de cvs
df     = pd.read_csv("states.csv") 
df_ind = pd.read_csv("indices_pobreza_consolidado.csv")


## Sidebar com Eplicações Propostas(Titulo, Autor, e Extras(SelectBox dos Municípios))
with st.sidebar:
    st.title("Dashboard - Municípios e seus Índices(2019)")
    # Puxa os Municipios do Dataframe
    option = st.selectbox("Selecione o Estado", df["UF"].unique()) 
# Sidebar com Nome e PDITA
st.sidebar.header("Autor")
st.sidebar.markdown("Miguel dos Santos Silva")
st.sidebar.markdown("PDITA303")


## Filtro de DataFrame(UF)
filtered_UF = df[df['UF'] == option]


## Agregação data para uso
aggregated_data = df.groupby("UF").agg({
    "Capital": "first",               # Capital
    "Population": "sum",            # Soma da População total
    "Area": "sum",                  # Soma da área total
    "Demographic Density": "mean",  # Média da densidade demográfica
    "Cities count": "sum",          # Soma do número de cidades
    "GDP": "mean",                  # Média do PIB
    "GDP rate": "mean"              # Média do Crescimento do PIB
}).reset_index()


## Métricas
st.subheader("Métricas")
col_capital, col_density, col_city, col_GDP = st.columns(4)
capital = col_capital.metric("Capital", 
               f"{aggregated_data.loc[aggregated_data['UF'] == option, 'Capital'].values[0]}")
# Densidade Demográfica
densidade_demografica = col_density.metric("Densidade Demográfica", 
               f"{aggregated_data.loc[aggregated_data['UF'] == option, 'Demographic Density'].values[0]} hab/km²") 
# Total de Cidades por Cidade
cidades = col_city.metric("Número de Cidades", 
               f"{aggregated_data.loc[aggregated_data['UF'] == option, 'Cities count'].values[0]}")     
# Metricas do PIB                                                        
pib = col_GDP.metric("PIB", 
               f"{aggregated_data.loc[aggregated_data['UF'] == option, 'GDP'].values[0]} BRL", 
               f"{aggregated_data.loc[aggregated_data['UF'] == option, 'GDP rate'].values[0]}% de Crescimento")


#____________ Gráficos ____________#

### Gráfico 1
fig_bar1 = px.bar(
    filtered_UF, x='UF',y=['Population', 'Area'], barmode='group', title=f"Comparação de População por área do Estado {option}")

### Gráfico de Pizza(DataFrame "artificial"(Criado com base em dados pesquisados))
data_pizza = {'Categoria': ['Pobreza', 'Extrema Pobreza', 'Vulnerabilidade'],'Porcentagem': [0.04, 0.19, 0.23]}
df_pizza   = pd.DataFrame(data_pizza)
fig_pie    = px.pie(df_pizza, values='Porcentagem', names='Categoria', title="Distribuição de Pobreza, Extrema Pobreza e Vulnerabilidade(Ano)",
                 color_discrete_sequence=['#BD2A2E', '#F24607', '#EAF205']) # Vaiável que armazena o gráfico de pizza

### Gráfico 2(Uso do plotly.graph_objs)
data     = [go.Bar(x=['PIB', 'Pobreza'], y=filtered_UF[['GDP rate', 'Poverty']].iloc[0].values, marker=dict(color=['#49D907', '#D90404']))]
#Layout do gráfico
layout   = go.Layout(title=f"Comparação de PIB e Pobreza para {option}", xaxis=dict(title='Indicadores'), yaxis=dict(title='Valores')) 
#Criação do Objeto  
fig_bar2 = go.Figure(data=data, layout=layout)                           

### Gráfico Linhas
fig_line = px.line(df_ind, x='referencia', y=['pobreza', 'extrema_pobreza', 'familias_pobreza', 'familias_extrema_pobreza'], 
                   title='Evolução da Pobreza e Extrema Pobreza', color_discrete_sequence=['#04D924', '#0903A6', '#F2B705', '#D9042B'])

## Mapa Populacional
fig_map  = px.scatter_geo(df, lat='Latitude', lon='Longitude', hover_name='Capital', text='Capital',projection="natural earth",
                         size='Population', size_max=20, color_continuous_scale='Viridis')


###### Exibição de Todo Conteúdo

# Exibição do Primeiro e Segundo Gráfico
st.subheader("Informações")
col_figbar1, col_figpie = st.columns(2) 

col_figbar1.plotly_chart(fig_bar1)        #Line 73
col_figpie.plotly_chart(fig_pie)          #Line 77

col_figbar2, col_figline = st.columns(2)   
col_figbar2.plotly_chart(fig_bar2)        #Line 83
col_figline.plotly_chart(fig_line)        #Line 90

# Exibição das Informações Gerais
st.subheader("Informações Gerais")
st.write(filtered_UF)                     #Line 38

# Exibição do Mapa e da Descrição
st.subheader("Mapa do Brasil com as capitais dos Estados")
col_fig_map, col_txt = st.columns([1, 1])
col_fig_map.plotly_chart(fig_map)         #Line 94               
col_txt.write("Esse mapa contém as informações populacionais de todas as capitais brasileiras, além de indicar População, \
              Latitude e Longitude de cada Estado brasileiro, para analisar o conteúdo aproxime-se do mapa do Brasil através do zoom.")
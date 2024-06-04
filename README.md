# 🇧🇷 Dashboard de Índices brasileiros
Esse Dashboard apresenta índices brasileiros baseados em métricas, indicando os dados presentes no arquivo csv baseado no estado escolhido.

## Instruções e Instalação
O Dashboard foi criado utilizando a versão 3.12.3 do Python.
#
Certifique-se de ter todas essas bibliotecas instaladas:
[Pandas](https://pandas.pydata.org/), 
[Plotly](https://plotly.com/graphing-libraries/), 
[Streamlit](https://streamlit.io/)
Para instalar as Bibliotecas pelo terminal, utilize o seguinte comando:
```
pip install pandas plotly streamlit
```
#
Para executar o Dashboard utilize o seguinte comando no terminal:
```
streamlit run brasil_dashboard.py
```
#
## Estruturação
| Arquivo   | Descrição |
| :-------- | :------- |
| `brasil_dashboard.py.py`  | Arquivo Principal na linguagem Python. Contém a estrutura do Dashbard, Utilizando manipulação de dados com a biblioteca Pnadas, Criação de Gráficos com plotly, e manipulação gráfica principal com Streamlit.    |
| `styles.css` | Contrúdo para estilização do Dashboard utilizando CSS. |
| `indices_pobreza_consolidado.csv`   | Base de dados indicando os indices de pobreza.   |
| `states.csv`   | Base de dados indicando os índices brasileiros.   |
#
## Dados
### indices_pobreza_consolidado.csv


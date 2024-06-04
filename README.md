# 📈🇧🇷 Dashboard de Índices brasileiros
Esse Dashboard apresenta índices brasileiros baseados em métricas, indicando os dados presentes no arquivo csv baseado no estado escolhido.
#
### Instruções e Instalação
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
### Estruturação
| Arquivo   | Descrição |
| :-------- | :------- |
| `brasil_dashboard.py.py`  | Arquivo Principal na linguagem Python. Contém a estrutura do Dashbard, Utilizando manipulação de dados com a biblioteca Pnadas, Criação de Gráficos com plotly, e manipulação gráfica principal com Streamlit.    |
| `styles.css` | Contrúdo para estilização do Dashboard utilizando CSS. |
| `indices_pobreza_consolidado.csv`   | Base de dados indicando os indices de pobreza.   |
| `states.csv`   | Base de dados indicando os índices brasileiros.   |
#
### 📊Dados utilizados(Apenas os principais dados extraídos)
## indices_pobreza_consolidado.csv
* pobreza: Número total de pessoas em estado de pobreza.
* extrema_pobreza: Número total de pessoas em estado de extrema pobreza.
* familias_pobreza: Número de famílias em estado de pobreza.
* familias_extrema_pobreza: Número de famílias em estado de extrema pobreza.
#
## states.csv
* Capital: Capitais dos estados brasileiros.                
* Population: População total por estado.            
* Area: Área por território.
* Demographic Density: Densidade Demográfica é a medida expressa pela relação entre a população e a superfície do território.
* Cities count: Soma total de Cidades baseada no Estado.         
* GDP: PIB(Produto Interno Bruto) que é a soma de todos os bens e serviços produzidos em uma região.                
* GDP rate: Taxa de Crescimento do PIB por região.
#
### Contato
[Linkedin](https://www.linkedin.com/in/miguel-santos-17b931259/)
Email: miguelsantoss006@gmail.com

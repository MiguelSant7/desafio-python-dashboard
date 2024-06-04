# 🇧🇷 Dashboard de Índices brasileiros
Esse Dashboard apresenta índices brasileiros baseados em métricas, indicando os dados presentes no arquivo csv baseado no estado escolhido.

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
### Estrutura do Projeto
| Arquivo   | Descrição |
| :-------- | :------- |
| `brasil_dashboard.py.py`  | Este é o arquivo principal do projeto. Ele contém as funcionalidades do dashboard, entre elas a manipulação de dados com Pandas, criação das visualizações com Plotly, e manipulação de widgets do Streamlit.    |
| `styles.css` | A estilização de elementos com CSS. Note que o nome das classes está associada aos nomes de widgets do Streamlit |
| `indices_pobreza_consolidado.csv`   | Base de dados utilizada no projeto. Maiores detalhes a seguir.   |
| `states.csv`   | Base de dados utilizada no projeto. Maiores detalhes a seguir.   |


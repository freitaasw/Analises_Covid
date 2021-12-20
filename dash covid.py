import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df_vacinacao = pd.read_csv('vaccination-data.csv')
df_vacinacao.head(3)

df_casos = pd.read_csv('WHO-COVID-19-global-table-data.csv')
df_casos.head()

df_casos_time = pd.read_csv('WHO-COVID-19-global-data.csv')
df_casos_time.head(3)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)


fig = px.choropleth(df_vacinacao, locations = "ISO3",
                    color = "PERSONS_FULLY_VACCINATED_PER100", # lifeExp is a column of gapminder
                    hover_name = "COUNTRY", # column to add to hover information
                    color_continuous_scale="Reds",
                    range_color=(0, 100), labels={'PERSONS_FULLY_VACCINATED_PER100':'Quantidade (%)'})
fig.update_layout(title={'text' : 'Relação de pessoas totalmente vacinas de cada país', 'y': 0.95, 'x': 0.5})


fig1 = px.choropleth(df_vacinacao, locations = "ISO3",
                    color = "PERSONS_VACCINATED_1PLUS_DOSE_PER100", # lifeExp is a column of gapminder
                    hover_name = "COUNTRY", # column to add to hover information
                    color_continuous_scale="Reds",
                    range_color=(0, 100), labels={'PERSONS_VACCINATED_1PLUS_DOSE_PER100':'Quantidade (%)'})
fig1.update_layout(title={'text' : 'Relação de pessoas vacinadas com ao menos um dose', 'y': 0.95, 'x': 0.5})


fig2 = px.choropleth(df_vacinacao, locations = "ISO3",
                    color = "NUMBER_VACCINES_TYPES_USED", # lifeExp is a column of gapminder
                    hover_name = "VACCINES_USED", # column to add to hover information
                    color_continuous_scale="Reds", range_color=(0, 6),
                    labels = {'NUMBER_VACCINES_TYPES_USED':'Quantidade'})
fig2.update_layout(title={'text' : 'Países com maior número de tipos de vacinas utilizadas contra a Covid-19', 'y': 0.95, 'x': 0.5})


df_groupby = df_casos.iloc[1:11]
fig3 = px.bar(df_groupby, x=df_groupby.index, y='WHO Region',
             labels={'index': 'Países', 'WHO Region': 'Quantidade de casos'},
             color_discrete_sequence=px.colors.qualitative.T10, template='plotly_white', text='WHO Region')
fig3.update_traces(textposition='inside',texttemplate='%{text:.3s}')
fig3.update_layout(title={'text' : 'Países com maior número de casos da Covid-19', 'y': 0.95, 'x': 0.5})


fig4 = px.bar(df_groupby, x=df_groupby.index, y='Cases - cumulative total per 100000 population',
             labels={'index': 'Países', 'Cases - cumulative total per 100000 population': 'Quantidade de casos'},
             color_discrete_sequence=px.colors.qualitative.T10, template='plotly_white', text='Cases - cumulative total per 100000 population')
fig4.update_traces(textposition='inside',texttemplate='%{text:.3s}')
fig4.update_layout(title={'text' : 'Número de casos novos da Covid-19 na útilma semana', 'y': 0.95, 'x': 0.5})


fig5 = px.bar(df_groupby, x=df_groupby.index, y='Cases - newly reported in last 24 hours',
             labels={'index': 'Países', 'Cases - newly reported in last 24 hours': 'Quantidade total de mortes'},
             color_discrete_sequence=px.colors.qualitative.T10, template='plotly_white', 
             text='Cases - newly reported in last 24 hours')
fig5.update_traces(textposition='inside',texttemplate='%{text:.3s}')
fig5.update_layout(title={'text' : 'Países com maior número de mortes pela Covid-19', 'y': 0.95, 'x': 0.5})


fig6 = px.bar(df_groupby, x=df_groupby.index, y='Deaths - cumulative total per 100000 population',
             labels={'index': 'Países', 'Deaths - cumulative total per 100000 population': 'Quantidade de mortes'},
             color_discrete_sequence=px.colors.qualitative.T10, template='plotly_white', text='Deaths - cumulative total per 100000 population')
fig6.update_traces(textposition='inside',texttemplate='%{text:.3s}')
fig6.update_layout(title={'text' : 'Número de novas mortes pela Covid-19 na útilma semana', 'y': 0.95, 'x': 0.5})


df_groupby = df_casos_time.set_index('Country_code')
df_groupby = df_groupby.loc[['BR', 'US', 'IN', 'RU', 'GB', 'TR', 'FR', 'IR', 'DE', 'AR']]
df_groupby['Date_reported'] = pd.to_datetime(df_groupby['Date_reported'])
df_groupby = df_groupby.set_index('Date_reported')
df_groupby['Cumulative_cases'] = df_groupby['Cumulative_cases'].apply(lambda x: float(x))


fig7 = px.line(df_groupby, x = df_groupby.index, y = 'Cumulative_cases', color = 'Country',
              labels = {'Date_reported': 'Período', 'Cumulative_cases': 'Casos acumulados', 'Country': 'País'},
              color_discrete_sequence=px.colors.qualitative.T10, template='gridon')
fig7.update_layout(title={'text' : 'Evolução da quantidade de casos da Covid-19 no Brasil', 'y': 0.95, 'x': 0.5})


fig8 = px.line(df_groupby, x = df_groupby.index, y = 'Cumulative_deaths', color = 'Country',
              labels = {'Date_reported': 'Período', 'Cumulative_deaths': 'Mortes acumuladas', 'Country': 'País'},
              color_discrete_sequence=px.colors.qualitative.T10, template='gridon')
fig8.update_layout(title={'text' : 'Evolução da quantidade de mortes pela Covid-19 no Brasil', 'y': 0.95, 'x': 0.5})


df_groupby = df_casos_time.set_index('Country_code')
df_groupby = df_groupby.loc['BR']
df_groupby['Date_reported'] = pd.to_datetime(df_groupby['Date_reported'])
df_groupby = df_groupby.set_index('Date_reported')
df_groupby['Cumulative_cases'] = df_groupby['Cumulative_cases'].apply(lambda x: float(x))
df_groupby['Cumulative_cases']=df_groupby['Cumulative_cases']/df_groupby['Cumulative_cases'].max()
df_groupby['Cumulative_deaths']=df_groupby['Cumulative_deaths']/df_groupby['Cumulative_deaths'].max()


fig9 = px.line(df_groupby, x = df_groupby.index, y = 'Cumulative_cases', color = 'Country',
              labels = {'Date_reported': 'Período', 'Cumulative_cases': 'Casos x Mortes', 'Country': 'Legenda'},
              color_discrete_sequence=px.colors.qualitative.T10, template='gridon')
fig9.update_layout(title={'text' : 'Relação entre casos e mortes pela Covid-19 no Brasil', 'y': 0.95, 'x': 0.5})
fig9.add_trace(go. Line(x=df_groupby.index, y=df_groupby['Cumulative_deaths']))


app.layout = html.Div(children=[
    html.H1(children='Análises de dados da Covid-19'
     ),
    
    dcc.Graph(
        id='example-graph',
        figure=fig
        ),
    dcc.Graph(
        id='example-graph-1',
        figure=fig1
        )
    
    
    ])


if __name__ == '__main__':
    app.run_server(debug=True)










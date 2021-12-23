import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Importando datasets
df_vacinacao = pd.read_csv('vaccination-data.csv')

df_casos = pd.read_csv('WHO-COVID-19-global-table-data.csv')

df_casos_time = pd.read_csv('WHO-COVID-19-global-data.csv')

# Preprocessando os dados para os gráficos de linhas
df_groupby1 = df_casos_time.set_index('Country_code')
df_groupby1 = df_groupby1.loc[[ 'AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AG', 'AR', 'AM', 'AW','AU', 'AT', 
        'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ','BM', 'BT', 'BO', 'XA', 'BA', 'BW', 'BR', 'VG', 
        'BN', 'BG', 'BF', 'BI', 'CV', 'KH', 'CM', 'CA', 'KY', 'CF', 'TD', 'CL', 'CN', 'CO','KM', 'CG', 'CK', 
        'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'KP','CD', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 
        'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 
        'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'VA', 'HN', 'HU', 'IS', 'IN', 'ID', 
        'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE','KI', 'XK', 'KW', 'KG', 'LA', 
        'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR',
        'MU', 'YT', 'MX', 'FM', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 
        'NE', 'NG', 'NU', 'MK', 'MP', 'NO', 'PS', 'OM', ' ', 'PK', 'PW', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 
        'PL', 'PT', 'PR', 'QA', 'KR', 'MD', 'RE', 'RO', 'RU', 'RW', 'XC', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 
        'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'XB', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 
        'SS', 'ES', 'LK', 'SD', 'SR', 'SE', 'CH', 'SY', 'TJ', 'TH', 'GB', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 
        'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'TZ', 'US', 'VI', 'UY', 'UZ', 'VU', 'VE', 'VN', 'WF', 'YE', 'ZM', 'ZW']]
df_groupby1 = df_groupby1.reset_index()
df_groupby1['Date_reported'] = pd.to_datetime(df_groupby1['Date_reported'])

### Criando os gráficos ###

# Gráfico 1
fig = px.choropleth(df_vacinacao, locations = "ISO3", color = "PERSONS_FULLY_VACCINATED_PER100", 
                    hover_name = "COUNTRY", color_continuous_scale="Reds",
                    range_color=(0, 100), labels={'PERSONS_FULLY_VACCINATED_PER100':'Quant. (%)'})
fig.update_layout(autosize=True, margin=go.layout.Margin(l=0, r=0, t=17, b=17), 
                  showlegend=False)

# Gráfico 2
fig1 = px.choropleth(df_vacinacao, locations = "ISO3", color = "PERSONS_VACCINATED_1PLUS_DOSE_PER100", 
                    hover_name = "COUNTRY", color_continuous_scale="Reds",
                    range_color=(0, 100), labels={'PERSONS_VACCINATED_1PLUS_DOSE_PER100':'Quant. (%)'})
fig1.update_layout(autosize=True, margin=go.layout.Margin(l=0, r=0, t=17, b=17), 
                   showlegend=False)

# Gráfico 3
fig2 = px.choropleth(df_vacinacao, locations = "ISO3", color = "NUMBER_VACCINES_TYPES_USED", 
                    hover_name = "VACCINES_USED", color_continuous_scale="Reds", range_color=(0, 6),
                    labels = {'NUMBER_VACCINES_TYPES_USED':'Quantidade'})
fig2.update_layout(autosize=True, margin=go.layout.Margin(l=0, r=0, t=17, b=17),
                   showlegend=False)

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

# Preprocessando os dados
df_groupby = df_casos_time.set_index('Country_code')
df_groupby = df_groupby.loc['BR'].reset_index()
df_groupby['Date_reported'] = pd.to_datetime(df_groupby['Date_reported'])
df_groupby = df_groupby.set_index('Date_reported')
df_groupby['Cumulative_cases']=df_groupby['Cumulative_cases']/df_groupby['Cumulative_cases'].max()
df_groupby['Cumulative_deaths']=df_groupby['Cumulative_deaths']/df_groupby['Cumulative_deaths'].max()

# Gráfico
fig9 = px.line(df_groupby, x = df_groupby.index, y = 'Cumulative_cases', color = 'Country',
              labels = {'Date_reported': 'Período', 'Cumulative_cases': 'Casos x Mortes', 'Country': 'Legenda'},
              color_discrete_sequence=px.colors.qualitative.T10, template='gridon')
fig9.add_trace(go.Line(x=df_groupby.index, y=df_groupby['Cumulative_deaths']))


# Criando o dashboard
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

app.layout = dbc.Container([
    
    dbc.Row(
        dbc.Col(html.H1("Dados da Covid-9 no mundo",
                        className='text-center text-primary mb-4'),
                width=12)
    ), 
    
    dbc.Row(
        dbc.Col([
            html.H1("Dados da Vacinação"),
            dcc.Dropdown(
                id= 'dropdown1',
                options= [
                    {'label' : 'Totalmente Vacinados', 'value' : 'Totalmente Vacinados'},
                    {'label' : 'Parcialmente Vacinados', 'value' : 'Parcialmente Vacinados'},
                    {'label' : 'Quantidade de Vacinas Utilizadas', 'value' : 'Vacinas Utilizadas'}
                ],
                value='Totalmente Vacinados'
            ),   
            dcc.Graph(id="choropleth-map1", figure= fig
            )       
        ])   
    ),
    
    dbc.Row([
        html.H1("Dados dos casos e mortes"),
        dbc.Col([
            dcc.Dropdown(id='dropdown2', multi=True, value=['BR', 'US', 'IN', 'RU', 'GB', 'TR', 'FR', 'IR', 'DE', 'AR'],
                         options=[{'label':x, 'value':x}
                                  for x in sorted(df_groupby1['Country_code'].unique())],
                         ),
            dcc.Graph(id='line-fig7', figure={})
        ]),
        dbc.Col([
            dcc.Dropdown(id='dropdown3', multi=True, value=['BR', 'US', 'IN', 'RU', 'GB', 'TR', 'FR', 'IR', 'DE', 'AR'],
                         options=[{'label':x, 'value':x}
                                  for x in sorted(df_groupby1['Country_code'].unique())],
                         ),
            dcc.Graph(id='line-fig8', figure={})
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H1("Histogramas dados em 03/12/2021"),
                dcc.Dropdown(
                    id= 'dropdown4',
                    options= [
                        {'label' : 'Quantidade total de casos', 'value' : 'Quantidade total de casos'},
                        {'label' : 'Novos casos na última semana', 'value' : 'Novos casos na última semana'},
                        {'label' : 'Quantidade total de mortes', 'value' : 'Quantidade total de mortes'},
                        {'label' : 'Novas mortes na última semana', 'value' : 'Novas mortes na última semana'}
                    ],
                    value='Quantidade total de casos'
                ),   
                dcc.Graph(id="figure3", figure= fig3
            ) 
        ])
    ]),
    
    dbc.Row(
        dbc.Col([
            html.H1("Relação de caso e mortes pela Coovid-19 no Brasil"),  
            dcc.Graph(id="fig9", figure= fig9
            )       
        ])   
    ),
    
], fluid=True)

@app.callback(
    Output(component_id='choropleth-map1', component_property='figure'),
    Input(component_id='dropdown1', component_property='value')
)
def changeText(value):
    if value == 'Totalmente Vacinados':
        return fig
    elif value == 'Parcialmente Vacinados':
        return fig1
    else:
        return fig2

# Line chart - multiple
@app.callback(
    Output('line-fig7', 'figure'),
    Input('dropdown2', 'value')
)
def update_graph(stock_slctd):
    # Gráfico 
    df_groupby11 = df_groupby1[df_groupby1['Country_code'].isin(stock_slctd)]
    fig7 = px.line(df_groupby11, x = 'Date_reported', y = 'Cumulative_cases', color = 'Country_code',
                  labels = {'Date_reported': 'Período', 'Cumulative_cases': 'Casos acumulados', 'Country_code': 'País'},
                  color_discrete_sequence=px.colors.qualitative.T10, template='gridon')
    fig7.update_layout(title={'text' : 'Evolução da quantidade de casos da Covid-19 no mundo', 'y': 0.95, 'x': 0.5})
    return fig7

# Line chart - multiple
@app.callback(
    Output('line-fig8', 'figure'),
    Input('dropdown3', 'value')
)
def update_graph(stock_slctd):
    # Gráfico 
    df_groupby11 = df_groupby1[df_groupby1['Country_code'].isin(stock_slctd)]
    fig8 = px.line(df_groupby11, x = 'Date_reported', y = 'Cumulative_deaths', color = 'Country_code',
              labels = {'Date_reported': 'Período', 'Cumulative_deaths': 'Mortes acumuladas', 'Country_code': 'País'},
              color_discrete_sequence=px.colors.qualitative.T10, template='gridon')
    fig8.update_layout(title={'text' : 'Evolução da quantidade de mortes pela Covid-19 no mundo', 'y': 0.95, 'x': 0.5})
    return fig8

# Line chart - multiple
@app.callback(
    Output(component_id='figure3', component_property='figure'),
    Input(component_id='dropdown4', component_property='value')
)
def update_graph(value):
    if value == 'Quantidade total de casos':
        return fig3
    elif value == 'Novos casos na última semana':
        return fig4
    elif value == 'Quantidade total de mortes':
        return fig5
    else:
        return fig6 

    
if __name__ == '__main__':
    app.run_server()
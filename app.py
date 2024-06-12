import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

# Carregar a base de dados
df = pd.read_csv(r'predictive_maintenance.csv')

# Criar o aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definir o layout do dashboard
app.layout = html.Div(children=[
    html.H1(children="Dashboard de Manutenção Preditiva"),

    # Seção de filtros
    dbc.Row([
        dbc.Col([
            html.Label("Selecione o Tipo de Produto:"),
            dcc.Dropdown(
                id='product-type-dropdown',
                options=[{'label': i, 'value': i} for i in df['Type'].unique()],
                value='M'
            ),
        ], width=3),
        dbc.Col([
            html.Label("Selecione o Tipo de Falha:"),
            dcc.Dropdown(
                id='failure-type-dropdown',
                options=[{'label': i, 'value': i} for i in df['Failure Type'].unique()],
                value='No Failure'
            ),
        ], width=3),
        dbc.Col([
            html.Label("Faixa de Tempo de Desgaste da Ferramenta:"),
            dcc.RangeSlider(
                id='tool-wear-slider',
                min=df['Tool wear [min]'].min(),
                max=df['Tool wear [min]'].max(),
                step=1,
                value=[df['Tool wear [min]'].min(), df['Tool wear [min]'].max()]
            ),
        ], width=6),
    ]),

    # Seção de gráficos
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='temperature-graph'),
        ], width=6),
        dbc.Col([
            dcc.Graph(id='speed-graph'),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='torque-graph'),
        ], width=6),
        dbc.Col([
            dcc.Graph(id='wear-graph'),
        ], width=6),
    ]),
], style={'padding': '20px'})

# Definir as funções de callback
@app.callback(
    Output('temperature-graph', 'figure'),
    Input('product-type-dropdown', 'value'),
    Input('failure-type-dropdown', 'value'),
    Input('tool-wear-slider', 'value')
)
def update_temperature_graph(product_type, failure_type, tool_wear_range):
    filtered_df = df[
        (df['Type'] == product_type) &
        (df['Failure Type'] == failure_type) &
        (df['Tool wear [min]'] >= tool_wear_range[0]) &
        (df['Tool wear [min]'] <= tool_wear_range[1])
    ]

    fig = go.Figure(data=[
        go.Scatter(
            x=filtered_df['Tool wear [min]'],
            y=filtered_df['Air temperature [K]'],
            mode='lines+markers',
            name='Temperatura do Ar'
        ),
        go.Scatter(
            x=filtered_df['Tool wear [min]'],
            y=filtered_df['Process temperature [K]'],
            mode='lines+markers',
            name='Temperatura do Processo'
        )
    ])
    fig.update_layout(
        title="Temperatura do Ar e Processo vs. Tempo de Desgaste da Ferramenta",
        xaxis_title="Tempo de Desgaste da Ferramenta [min]",
        yaxis_title="Temperatura [K]"
    )
    return fig

@app.callback(
    Output('speed-graph', 'figure'),
    Input('product-type-dropdown', 'value'),
    Input('failure-type-dropdown', 'value'),
    Input('tool-wear-slider', 'value')
)
def update_speed_graph(product_type, failure_type, tool_wear_range):
    filtered_df = df[
        (df['Type'] == product_type) &
        (df['Failure Type'] == failure_type) &
        (df['Tool wear [min]'] >= tool_wear_range[0]) &
        (df['Tool wear [min]'] <= tool_wear_range[1])
    ]

    fig = go.Figure(data=[
        go.Scatter(
            x=filtered_df['Tool wear [min]'],
            y=filtered_df['Rotational speed [rpm]'],
            mode='lines+markers',
            name='Velocidade de Rotação'
        )
    ])
    fig.update_layout(
        title="Velocidade de Rotação vs. Tempo de Desgaste da Ferramenta",
        xaxis_title="Tempo de Desgaste da Ferramenta [min]",
        yaxis_title="Velocidade de Rotação [rpm]"
    )
    return fig

@app.callback(
    Output('torque-graph', 'figure'),
    Input('product-type-dropdown', 'value'),
    Input('failure-type-dropdown', 'value'),
    Input('tool-wear-slider', 'value')
)
def update_torque_graph(product_type, failure_type, tool_wear_range):
    filtered_df = df[
        (df['Type'] == product_type) &
        (df['Failure Type'] == failure_type) &
        (df['Tool wear [min]'] >= tool_wear_range[0]) &
        (df['Tool wear [min]'] <= tool_wear_range[1])
    ]

    fig = go.Figure(data=[
        go.Scatter(
            x=filtered_df['Tool wear [min]'],
            y=filtered_df['Torque [Nm]'],
            mode='lines+markers',
            name='Torque'
        )
    ])
    fig.update_layout(
        title="Torque vs. Tempo de Desgaste da Ferramenta",
        xaxis_title="Tempo de Desgaste da Ferramenta [min]",
        yaxis_title="Torque [Nm]"
    )
    return fig

@app.callback(
    Output('wear-graph', 'figure'),
    Input('product-type-dropdown', 'value'),
    Input('failure-type-dropdown', 'value'),
    Input('tool-wear-slider', 'value')
)
def update_wear_graph(product_type, failure_type, tool_wear_range):
    filtered_df = df[
        (df['Type'] == product_type) &
        (df['Failure Type'] == failure_type) &
        (df['Tool wear [min]'] >= tool_wear_range[0]) &
        (df['Tool wear [min]'] <= tool_wear_range[1])
    ]

    fig = go.Figure(data=[
        go.Scatter(
            x=filtered_df['Tool wear [min]'],
            y=filtered_df['Tool wear [min]'],
            mode='lines+markers',
            name='Desgaste da Ferramenta'
        )
    ])
    fig.update_layout(
        title="Desgaste da Ferramenta vs. Tempo de Desgaste da Ferramenta",
        xaxis_title="Tempo de Desgaste da Ferramenta [min]",
        yaxis_title="Desgaste da Ferramenta [min]"
    )
    return fig

# Executar o aplicativo Dash
if __name__ == '__main__':
    app.run_server(debug=True)

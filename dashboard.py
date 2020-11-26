# available_indicators = df['Indicator Name'].unique()

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('sandbox.csv')

app.layout = html.Div([
    html.H6("Tableau de bord interactif"),
    html.Div(["Numéro de dossier",
        dcc.Input(
            id='cust_id',
            type='number',
            value=101
    )]),
    html.Table([
        html.Tr([html.Td(['SCORE v2:   ']), html.Td(id='score')]),
        html.Tr([html.Td(['DECISION :']), html.Td(id='decision')])
    ]),
])


@app.callback(
    Output('score', 'children'),
    Output('decision', 'children'),
    Input('cust_id', 'value'))
def callback_a(x):
    dff = df[df['SK_ID_CURR'] == x]
    return dff['SCORE'], dff['DECISION']


if __name__ == '__main__':
    app.run_server(debug=True)
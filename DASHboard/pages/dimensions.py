from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.Br(),
    dcc.Link('Next page', href='/population_bias')
])


from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.Br(),
    html.Ul([
        html.Li("Confirmatory statistics / statistical inference works with known categories."),
        html.Li("Representativity means absence of bias (systematic error)."),
        html.Li("Statistical testing addresses random error.")
    ]),
    html.Br(),
])


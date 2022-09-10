from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

tab_eda = [html.P("Exploratory Data Analysis vs. Confirmatory Data Analysis")]
tab_bias = [html.P("Population and Bias")]
tab_dimension = [html.P("Dimensionality Reduction")]

layout = html.Div([
    html.H2("Example Questions"),
    html.P("Which statistical tests are suited to analyse group differences?"),
    html.P("Which statistical tests are suited to compare our sample to the German Census?"),
    html.P("What are the implications of sample bias that we need to keep in mind / "
           "discuss when drawing conclusions from the data?"),
    html.H2("Our Sub-questions"),
    dbc.Tabs([
        dbc.Tab(tab_eda, label="EDA vs CDA"),
        dbc.Tab(tab_bias, label="Population and Bias"),
        dbc.Tab(tab_dimension, label="Dimensionality Reduction")
    ])
    ]
)

from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

tab_eda = [html.Br(),
           html.P("Exploratory Data Analysis vs. Confirmatory Data Analysis."),
           html.Ul([
               html.Li("The distinction"),
               html.Li("Pitfalls"),
               html.Li("Remedy")
           ])]
tab_dimension = [html.Br(),
                 html.P("Dimensionality Reduction"),
                 html.Ul([
                     html.Li("A classic EDA technique"),
                     html.Li("Making data more manageable")
                 ])]
tab_bias = [html.Br(),
            html.P("Population and Bias"),
            html.Ul([
                html.Li("Correcting for sampling bias needed for CDA"),
                html.Li("Related topics of bias and comparison to other populations.")
            ])]

layout = html.Div([
    html.H2("Example Questions"),
    html.P("Which statistical tests are suited to analyse group differences?"),
    html.P("Which statistical tests are suited to compare our sample to the German Census?"),
    html.P("What are the implications of sample bias that we need to keep in mind / "
           "discuss when drawing conclusions from the data?"),
    html.H2("Our Sub-questions"),
    html.P("From an initial brainstorm, we came up with three related topics."),
    dbc.Tabs([
        dbc.Tab(tab_eda, label="EDA vs CDA"),
        dbc.Tab(tab_dimension, label="Dimensionality Reduction"),
        dbc.Tab(tab_bias, label="Population and Bias")
    ]),
    dcc.Link('Next page', href='/eda_cda')
])

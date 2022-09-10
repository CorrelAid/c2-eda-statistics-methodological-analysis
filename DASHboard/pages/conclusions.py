from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

layout = html.Div([
    html.H2("Next Steps"),
    html.H2("Presentation Template Questions"),
    dbc.Tabs([
        dbc.Tab(html.P("Already done."),
                label="Show and Tell"),
        dbc.Tab(html.P("Mainly in a Google Drive doc, but also here and in the repo readme."),
                label="Where Documented?"),
        dbc.Tab(html.P("Working with the provided database in the limited timeframe, "
                       "particularly given the need for data transformations."),
                label="Problems Encountered"),
        dbc.Tab(html.P("Only desk / theoretical research so far on our challenge."),
                label="Limitations"),
        dbc.Tab(html.P("Transformations of the data set to allow testing out our ideas."),
                label="To fix"),
        dbc.Tab(html.P("Further discussion with CfE about survey, i.e research, goals would be beneficial."),
                label="To improve"),
        dbc.Tab(html.P("Cross-fertilisation of ideas in our group discussion, remote data access, "
                       "data wrangling as a blocker for time critical activities."),
                label="Learnings")
    ]),
    dcc.Link('Back to start', href='/')
])


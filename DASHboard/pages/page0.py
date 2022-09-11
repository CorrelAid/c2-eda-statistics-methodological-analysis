from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.H2("Motivating Questions"),
    html.P("Which statistical analyses make sense with our data?"),
    html.P("Which methods can be used to derive which statements from the data?"),
    html.H2("Our Initial Solution Space"),
    html.Img(src="https://www.reactiongifs.com/r/weeds.gif", width="100%"),
    html.Br(),
    dcc.Link('Next page', href='/problem_definition')
])


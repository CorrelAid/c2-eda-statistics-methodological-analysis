from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.Br(),
    html.H2("Why make a distinction?"),
    html.Img(src="assets/spurious.jpeg", width="100%"),
    dcc.Link("From spurious correlations", href="http://www.tylervigen.com/spurious-correlations"),
    html.Br(),
    html.Br(),
    dcc.Link('Next page', href='/dimensionality')
])

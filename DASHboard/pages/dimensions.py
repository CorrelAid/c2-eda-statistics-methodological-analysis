from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.H2("Latent profile and latent class analysis"),
    html.Img(src="assets/01_EGA_Results.png", width="100%"),
    html.Img(src="assets/03_LPA.png", width="100%"),
    html.Br(),
    dcc.Link('Next page', href='/population_bias')
])


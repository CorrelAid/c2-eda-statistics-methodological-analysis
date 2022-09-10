import os
import sys
import importlib.util
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

# SETTINGS

# sidebar
sidebar_header = "Contents"
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# page content area
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# TODO: header style

# load page directory
pages = pd.read_csv(os.path.join('settings', 'page_directory.csv'))
# TODO: add data validation for pages: URLs should be unique, files should exist and header should be non-empty
# Failed validation on rows should lead to a warning message in the console and dropping them, but not a crash.
pages['url'].iloc[0] = ""  # force first page to act at the landing page

# import scripts for each page
page_dic = {}  # the page_dic dictionary is used to reference the pages programmatically
for page_script in pages.filename:
    module_name = page_script[:-3]
    module_path = os.path.join("pages", page_script)
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    page_dic[module.__name__] = module


# declare the Dash app
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# create page template
navlink_list = [dbc.NavLink(page['header'], href="/"+page['url'], active="exact") for index, page in pages.iterrows()]
sidebar = html.Div(
    [
        html.H2(sidebar_header, className="display-4"),
        html.Hr(),
        dbc.Nav(navlink_list, vertical=True, pills=True),
    ],
    style=SIDEBAR_STYLE,
)
content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    # find the page in the page directory
    if pathname == "" or pathname == "/":
        display_page = pages.iloc[0]
    else:
        try:
            display_page = pages[pages['url'] == pathname[1:]].iloc[0]
        except IndexError:
            # an IndexError is thrown if the pathname is not known
            return [html.H1("Page not found"),
                    html.P([f"The URL ending with ",
                            html.B(pathname[1:]),
                            " was not recognised. ",
                            dcc.Link("Click here", href='/'),
                            " or use the navigation bar."]),
                    ]
    return [html.H1(display_page.header), page_dic[display_page.filename[:-3]].layout]


if __name__ == '__main__':
    app.run_server(debug=True)

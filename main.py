from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import src.pages.dashboard_map as dashboard_map
import src.pages.dashboard_histogram as dashboard_histogram

# Création de l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.title = "Dashboard Vélib"

# Mise en page princiaple
app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh=False),  # Gère l'URL
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Données graphiques", href="/")),
                dbc.NavItem(dbc.NavLink("Données géographiques", href="/map")),
            ],
            brand="Vélib Dashboard",
            brand_href="/",
            color="dark",
            dark=True,
        ),
        html.Div(id="page-content"),  # Contenu des pages
    ],
    fluid=True,
)

# Charger les pages en fonction de l'URL
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/map":
        return dashboard_map.layout
    else:
        return dashboard_histogram.layout

if __name__ == "__main__":
    app.run_server(debug=True)

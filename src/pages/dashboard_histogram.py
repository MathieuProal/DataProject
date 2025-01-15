from dash import html, dcc
import dash_bootstrap_components as dbc
from src.components.histogram import create_histogram
from src.components.pie import create_pie

# Création des graphiques
histogram = create_histogram()
pie = create_pie()

# Contenu de la page
layout = dbc.Container(
    [
        html.H3("Dashboard", className="text-center"),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=histogram), width=6, style={"padding": "10px"}),
                dbc.Col(dcc.Graph(figure=pie), width=6, style={"padding": "10px"}),
            ]
        ),
    ],
    fluid=True,
)

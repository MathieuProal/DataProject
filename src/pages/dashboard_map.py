from dash import html
import dash_bootstrap_components as dbc
import src.components.map

# Création de la carte
#map_html = create_map()

# Contenu de la page
with open("src\components\map.html", "r", encoding="utf-8") as f:
    map_content = f.read()

layout = dbc.Container(
    [
        html.H3("Carte des Vélib", className="text-center"),
        html.Div(
            [
                html.Iframe(
                    srcDoc=map_content,
                    style={
                        "width": "100%",
                        "height": "500px",
                        "border": "3px solid #123456",
                        "borderRadius": "15px",
                        "boxShadow": "4px 4px 10px rgba(0, 0, 0, 0.2)",
                    },
                ),
            ],
            style={
                "padding": "15px",
                "border": "2px solid #888",
                "borderRadius": "15px",
                "backgroundColor": "#f8f9fa",
            },
        ),
    ]
)

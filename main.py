from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from src.components.histogram import create_histogram
from src.components.pie import create_pie
from src.utils.get_data import get_data
from src.utils.clean_data import clean_data

# Initialisation des variables
data_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
output_data_file = "data/raw/data_velib.csv"
datato_clean = "data/raw/data_velib.csv"
ourput_cleaned_data_file = "data/cleaned/cleaned_data_velib.csv"
map = "map1.html"

# Télécharge et nettoie les données
get_data(data_url, output_data_file)
clean_data(datato_clean, ourput_cleaned_data_file)

# Crée les graphiques
histogram = create_histogram()
pie = create_pie()

# Lire le contenu des fichiers header.html et footer.html
with open("header.html", "r", encoding="utf-8") as f:
    header_content = f.read()

with open("footer.html", "r", encoding="utf-8") as f:
    footer_content = f.read()

# Crée l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dashboard Vélib"

# Mise en page
app.layout = dbc.Container(
    [
        # En-tête
        dbc.Row(
            dbc.Col(
                dcc.Markdown(
                    header_content,
                    dangerously_allow_html=True,  # Autoriser l'HTML dans le Markdown
                )
            )
        ),
        # Ligne 1 : Carte interactive
        # Ligne 1 : Carte interactive
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H3("Carte Interactive", className="text-center"),
                            html.Iframe(
                                srcDoc=open(map, "r").read(),
                                style={
                                    "width": "100%",
                                    "height": "500px",  # Hauteur augmentée
                                    "border": "3px solid #123456",
                                    "borderRadius": "15px",  # Bordures arrondies
                                    "boxShadow": "4px 4px 10px rgba(0, 0, 0, 0.2)",  # Ombres portées
                                },
                            ),
                        ],
                        style={
                            "padding": "15px",
                            "border": "2px solid #888",  # Bordure externe pour séparer la carte
                            "borderRadius": "15px",
                            "backgroundColor": "#f8f9fa",  # Couleur de fond légèrement grise
                        },
                    ),
                    width=5,  # Carte légèrement plus large
                ),
                dbc.Col(width=7),  # Colonne vide pour ajustement
            ],
        ),

        # Ligne 2 : Histogramme et graphique circulaire
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(figure=histogram),
                    width=6,
                    style={"padding": "10px"},
                ),
                dbc.Col(
                    dcc.Graph(figure=pie),
                    width=6,
                    style={"padding": "10px"},
                ),
            ]
        ),
        # Pied de page
        dbc.Row(
            dbc.Col(
                dcc.Markdown(
                    footer_content,
                    dangerously_allow_html=True,  # Autoriser l'HTML dans le Markdown
                )
            )
        ),
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)

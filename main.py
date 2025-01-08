from dash import Dash, dcc, html
from src.components.histogram import create_histogram
from src.utils.get_data import get_data
from src.utils.clean_data import clean_data

# Initialisation des variables
data_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
output_data_file = "data/raw/data_velib.csv"
datato_clean = "data/raw/data_velib.csv"
ourput_cleaned_data_file = "data/cleaned/cleaned_data_velib.csv"

# Télécharge et nettoie les données
get_data(data_url, output_data_file)
clean_data(datato_clean, ourput_cleaned_data_file)

fig = create_histogram()
app = Dash(__name__)
app.title = "Dashboard Vélib"
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)

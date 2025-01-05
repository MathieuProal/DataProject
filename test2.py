import pandas as pd
import plotly.express as px

# Exemple de données
data = {
    'station_name': ['Station 1', 'Station 2', 'Station 3', 'Station 4', 'Station 5'],
    'bikes_available': [5, 15, 20, 10, 7],
}

# Charger les données dans un DataFrame
df = pd.DataFrame(data)

# Création de l'histogramme
fig = px.histogram(
    df,
    x="bikes_available",
    nbins=10,  # Nombre de classes dans l'histogramme
    title="Répartition des vélos disponibles",
    labels={"bikes_available": "Nombre de vélos disponibles"},
    template="plotly_white",
)

# Mise en page
fig.update_layout(
    xaxis_title="Nombre de vélos disponibles",
    yaxis_title="Nombre de stations",
    title_x=0.5,  # Centrer le titre
)

# Afficher l'histogramme
fig.show()

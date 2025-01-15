import folium
from folium.plugins import MarkerCluster
import pandas as pd
import io

# Afficher les points
def affichagePoint(coord1, coord2, texte, marker_cluster):
    point_coords = (float(coord1), float(coord2))
    folium.Marker(
        location=point_coords,
        popup=texte,
        icon=folium.Icon(color='darkblue', icon='bicycle', prefix='fa'),  # Utilisation d'icônes modernes
    ).add_to(marker_cluster)

# Créer la carte en retournant un html
def create_map():
    # Coordonnées de Paris
    coords = (48.8398094, 2.5840685)

    # Charger les données
    data = pd.read_csv('data/cleaned/cleaned_data_velib.csv', delimiter=',')

    # Création de la carte
    map = folium.Map(location=coords, tiles="CartoDB positron", zoom_start=12)

    # Cluster pour grouper les points proches
    marker_cluster = MarkerCluster().add_to(map)

    # Ajoute chaque points à la carte
    for index, ligne in data.iterrows():
        coord1, coord2 = ligne["Coordonnées géographiques"].split(",")
        if ligne["Station en fonctionnement"] == "OUI":
            affichagePoint(coord1, coord2, ligne["Nom station"], marker_cluster)

    # Sauvegarder la carte dans une variable HTML
    map_buffer = io.StringIO()
    map.save(map_buffer, close_file=False)
    map_html = map_buffer.getvalue()
    map_buffer.close()

    return map_html

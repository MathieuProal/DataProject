import folium
from folium.plugins import MarkerCluster
import pandas as pd
import io

# Fonction pour afficher les points
def affichagePoint(coord1, coord2, texte, marker_cluster):
    point_coords = (float(coord1), float(coord2))
    folium.Marker(
        location=point_coords,
        popup=texte,
        icon=folium.Icon(color='darkblue', icon='bicycle', prefix='fa'),  # Utilisation d'icônes modernes
    ).add_to(marker_cluster)

# Coordonnées de Paris
coords = (48.8398094, 2.5840685)

# Charger les données
csvRead = pd.read_csv('data/cleaned/cleaned_data_velib.csv', delimiter=",")

# Créer une carte interactive
map = folium.Map(location=coords, tiles="CartoDB positron", zoom_start=12)

# Ajouter un cluster pour grouper les points proches
marker_cluster = MarkerCluster().add_to(map)

# Ajouter des points à la carte
for index, ligne in csvRead.iterrows():
    coord1, coord2 = ligne["Coordonnées géographiques"].split(",")
    if ligne["Station en fonctionnement"] == "OUI":
        affichagePoint(coord1, coord2, ligne["Nom station"], marker_cluster)

# Sauvegarder la carte dans une variable HTML
map.save(outfile='src\components\map.html')
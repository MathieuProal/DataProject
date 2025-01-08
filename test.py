import folium
import geojson, geopandas, pandas

def affichagePoint(coord1, coord2, texte, map) :
    point_coords = (float(coord1), float(coord2))
    folium.Marker(
        location=point_coords,
        popup=texte, 
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(map)


# Coordonnées de Paris
coords = (48.8398094,2.5840685)
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=10)

csvRead = pandas.read_csv('data/raw/data_velib.csv', delimiter=";")

for index, ligne in csvRead.iterrows():
    coord1, coord2 = ligne['Coordonnées géographiques'].split(',')
    if (ligne['Station en fonctionnement']=="NON"):
        affichagePoint(coord1, coord2, ligne['Nom station'], map)

# marker cluster dans folium  
map.save(outfile='map1.html')
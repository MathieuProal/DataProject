import folium
import geojson, geopandas, pandas

def affichagePoint(coord1, coord2, texte, map) :
    print(coord1+" "+coord2)
    point_coords = (float(coord1), float(coord2))
    folium.Marker(
        location=point_coords,
        popup=texte, 
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(map)


# Coordonnées de Paris
coords = (48.8398094,2.5840685)
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=8)

csvRead = pandas.read_csv('velib-disponibilite-en-temps-reel.csv', delimiter=";")

for index, ligne in csvRead.iterrows():
    coord1, coord2 = ligne[11].split(',')
    if (ligne[2]=="NON"):
        affichagePoint(coord1, coord2, ligne['Nom station'], map)

map.save(outfile='map.html')


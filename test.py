import folium
import geojson, geopandas, pandas

def affichagePoint(coord1, coord2, texte, map) :
    print(coord1+" "+coord2)
    point_coords = (coord1, coord2)
    folium.Marker(
        location=point_coords,
        popup=texte, 
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(map)


coords = (48.8398094,2.5840685)
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=8)

csvRead = pandas.read_csv('velib-disponibilite-en-temps-reel.csv')
tailleCSV = csvRead.size
for i in range(0, tailleCSV-1):
    ligne = csvRead.iloc[i]
    coord1, coord2 = ligne['Coordonnées géographiques'].split(',')
    affichagePoint(48.8566, 2.3522, ligne['Nom station'], map)

map.save(outfile='map.html')


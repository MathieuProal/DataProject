import pandas as pd

# Récupère les données du fichier csv
data = pd.read_csv('../../data/raw/data_velib.csv', delimiter=";")

# Récupère uniquement les données nécessaire
cleaned_data = data[['Nom station', 'Nombre total vélos disponibles', 'Station en fonctionnement']]

# Enregistre les données nettoyé dans un nouveau fichier
cleaned_data.to_csv('../../data/cleaned/cleaned_data_velib.csv', index=False)
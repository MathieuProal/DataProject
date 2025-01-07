import pandas as pd

def clean_data(input_file, output_file):
    # Récupère les données du fichier csv
    data = pd.read_csv(input_file, delimiter=";")

    # Récupère uniquement les données nécessaires
    cleaned_data = data[['Nom station', 'Nombre total vélos disponibles', 'Station en fonctionnement']]

    # Enregistre les données nettoyées dans un nouveau fichier
    cleaned_data.to_csv(output_file, index=False)
    print("Les données ont été nettoyées")

if __name__ == "__main__":
    # Initialisation des variables
    input_file = "../../data/raw/data_velib.csv"
    output_file = "../../data/cleaned/cleaned_data_velib.csv"

    clean_data(input_file, output_file)

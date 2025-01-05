import requests

def download_csv(url, output_file):
    """
    Télécharge un fichier csv et l'enregistre dans le fichier donnée en paramètre.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si le téléchargement à échoué.
        
        with open(output_file, 'wb') as file:
            file.write(response.content)

    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors du téléchargement du fichier : {e}")

if __name__ == "__main__":
    csv_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
    output_path = "../../data/raw/data_velib.csv"
    
    download_csv(csv_url, output_path)

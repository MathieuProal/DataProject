import pandas as pd
import plotly.express as px

def create_histogram():
    # Récupération des données
    data = pd.read_csv('data/cleaned/cleaned_data_velib.csv', delimiter=',')

    # Charger les données dans un DataFrame
    df = pd.DataFrame(data)

    # Création de l'histogramme
    fig = px.histogram(
        df,
        x='Nombre total vélos disponibles',
        nbins=60,  # Nombre de classes dans l'histogramme
        title="Répartition des vélos disponibles",
        labels={'Nombre total vélos disponibles': "Nombre de vélos disponibles"},
        template="plotly_white",
    )

    # Mise en page
    fig.update_layout(
        xaxis_title="Nombre de vélos disponibles",
        yaxis_title="Nombre de stations",
        title_x=0.5,  # Centrer le titre
    )
    return fig

if __name__ == "__main__":
    fig = create_histogram()
    fig.show()

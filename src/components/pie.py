import pandas as pd
import plotly.express as px

def create_pie():
    # Récupération des données
    data = pd.read_csv('data/cleaned/cleaned_data_velib.csv', delimiter=',')

    # Charger les données dans un DataFrame
    df = pd.DataFrame(data)

    # Création du camembert
    fig = px.pie(
        df,
        values='Nombre total vélos disponibles', 
        names='Station en fonctionnement'
    )
    return fig

if __name__ == "__main__":
    fig = create_pie()
    fig.show()

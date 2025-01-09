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
        names='Station en fonctionnement',
        title="Répartition des vélos par statut des stations",
        color='Station en fonctionnement',  # Ajout de couleurs selon les catégories
        color_discrete_map={
            "OUI": "#28a745",  # Vert pour les stations en fonctionnement
            "NON": "#dc3545"   # Rouge pour les stations hors service
        },
        template="plotly_white",
    )

    # Mise en valeur des sections avec une "explosion"
    fig.update_traces(
        pull=[0.1 if name == "NON" else 0 for name in df['Station en fonctionnement']],
        textinfo="percent+label",  # Affiche pourcentage + label
        textfont=dict(size=14, family="Arial", color="black"),
        marker=dict(line=dict(color="#ffffff", width=2)),  # Bordures blanches pour plus de contraste
    )

    # Mise en page
    fig.update_layout(
        title={
            "text": "Répartition des vélos par statut des stations",
            "x": 0.5,  # Centrer le titre
            "xanchor": "center",
            "font": {"size": 20, "family": "Arial", "color": "#333"}
        },
        font=dict(family="Arial", size=14, color="#333"),
        legend=dict(
            title="Statut des stations",
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.1,
        ),
    )

    return fig

if __name__ == "__main__":
    fig = create_pie()
    fig.show()

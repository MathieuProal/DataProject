import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def create_histogram():
    # Récupération des données
    data = pd.read_csv('data/cleaned/cleaned_data_velib.csv', delimiter=',')

    # Charger les données dans un DataFrame
    df = pd.DataFrame(data)

    # Calcul de la moyenne des vélos disponibles
    mean_value = df['Nombre total vélos disponibles'].mean()

    # Création de l'histogramme
    fig = px.histogram(
        df,
        x='Nombre total vélos disponibles',
        nbins=10,  # Nombre de classes dans l'histogramme
        title="Répartition des vélos disponibles",
        labels={'Nombre total vélos disponibles': "Nombre de vélos disponibles"},
        template="plotly_white",
        color_discrete_sequence=['#1f77b4'],  # Couleur personnalisée
    )

    # Ajout d'une ligne de référence pour la moyenne
    fig.add_vline(
        x=mean_value,
        line_dash="dash",
        line_color="red",
        annotation_text="Moyenne",
        annotation_position="top right",
        annotation_font_size=12,
        annotation_font_color="red",
    )

    # Mise en page améliorée
    fig.update_layout(
        xaxis_title="Nombre de vélos disponibles",
        yaxis_title="Nombre de stations",
        title={
            "text": "Répartition des vélos disponibles",
            "x": 0.5,  # Centrer le titre
            "xanchor": "center",
            "font": {"size": 20, "family": "Arial", "color": "#1f77b4"},
        },
        font=dict(family="Arial", size=14, color="#333"),
        plot_bgcolor="#f8f9fa",  # Fond de l'histogramme
        paper_bgcolor="#ffffff",  # Fond de l'image
    )

    # Ajout d'annotations supplémentaires (optionnel)
   # fig.add_annotation(
      #  x=mean_value,
      #  y=max(fig.data[0].y) * 0.8,  # Position relative sur l'axe Y
      #  text=f"Moyenne: {mean_value:.2f}",
     #   showarrow=True,
       # arrowhead=2,
       # ax=-40,  # Décalage horizontal
       # ay=-30,  # Décalage vertical
      #  font=dict(size=12, color="red"),
    #    arrowcolor="red",
   # )

    # Amélioration des ticks et des barres
    fig.update_xaxes(
        tickangle=45,  # Inclinaison des étiquettes
        tickfont=dict(size=12, color="#333"),
        showgrid=True,
        gridcolor="#e9ecef",
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="#e9ecef",
    )

    return fig

if __name__ == "__main__":
    fig = create_histogram()
    fig.show()

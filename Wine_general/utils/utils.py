import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpld3
import numpy as np
import plotly.express as px


def gera_grafico(indice: int) -> None:
    df_Winedata = pd.read_csv('base/static/WineData.csv', sep=';')
    vinicolas = {
        1: 'Zorzal',
        2: 'Zepaltas',
        3: 'Yuntero',
        4: 'Wines & Winemakers',
        5: 'Weninger',
        6: 'Vite Colte',
        7: 'Thomas George',
        8: 'The Calling',
        9: 'Terras de Alter',
        10: 'Tarara',
        11: 'Stoller',
        12: 'Saviah'}
    df = df_Winedata[['winery', 'price', 'quality', 'pH', 'residual sugar', 'total sulfur dioxide', 'points']].dropna()
    grouped = df.groupby('winery')[
        ['price', 'quality', 'pH', 'residual sugar', 'total sulfur dioxide', 'points']].mean()
    grouped = grouped.drop_duplicates(subset=['quality'], keep='last')

    # Criar arrays únicos para cada coluna
    x_price = grouped['price'].values
    x_quality = grouped['quality'].values
    x_pH = grouped['pH'].values
    x_sugar = grouped['residual sugar'].values
    x_sulfur = grouped['total sulfur dioxide'].values
    x_points = grouped['points'].values

    fig, ax = plt.subplots(figsize=(10, 6))

    for index, row in grouped.iterrows():  # Define a opacidade da vinícola Zorzal
        print(index)
        if vinicolas.get(indice).lower() == index.lower():
            opacity = 1.0
        else:
            opacity = 0.2
        idx = np.where(grouped.index == index)[0][0]  # Encontrar o índice inteiro correspondente ao nome da vinícola

        ax.scatter(x_price[idx], index, label='Preço médio', s=100, alpha=opacity)
        ax.scatter(x_quality[idx], index, label='Qualidade', s=100, alpha=opacity)
        ax.scatter(x_pH[idx], index, label='pH', s=100, alpha=opacity)
        ax.scatter(x_sugar[idx], index, label='Açúcar residual', s=100, alpha=opacity)
        ax.scatter(x_sulfur[idx], index, label='Dióxido de enxofre total', s=100, alpha=opacity)
        ax.scatter(x_points[idx], index, label='Pontos', s=100, alpha=opacity)

    ax.set_title('Preço médio, qualidade, pH, açúcar residual, dióxido de enxofre total e pontos por vinícula')
    ax.set_ylabel('Vinícola')
    ax.legend()

    # Salvar o gráfico em uma variável
    plt.savefig('base/static/images/grafico.png')


import matplotlib
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.pyplot as mpld3
import numpy as np
import plotly.express as px
from googletrans import Translator
import psycopg2
from os import environ

matplotlib.use('Agg')


def gera_grafico(df_Winedata, indice: int) -> None:
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
    df = df_Winedata[['winery', 'price', 'quality', 'ph', 'residual_sugar', 'total_sulfur_dioxide', 'points']].dropna()
    grouped = df.groupby('winery')[
        ['price', 'quality', 'ph', 'residual_sugar', 'total_sulfur_dioxide', 'points']].mean()
    grouped = grouped.drop_duplicates(subset=['quality'], keep='last')

    # Criar arrays únicos para cada coluna
    x_price = grouped['price'].values
    x_quality = grouped['quality'].values
    x_pH = grouped['ph'].values
    x_sugar = grouped['residual_sugar'].values
    x_sulfur = grouped['total_sulfur_dioxide'].values
    x_points = grouped['points'].values

    fig, ax = plt.subplots(figsize=(10, 6))

    for index, row in grouped.iterrows():
        idx = np.where(grouped.index == index)[0][0]  # Encontrar o índice inteiro correspondente ao nome da vinícola
        if vinicolas.get(indice).lower() == index.lower():
            # Define a opacidade da vinícola
            opacity = 1.0
            ax.scatter(x_price[idx], index, label='Preço médio', s=100, alpha=opacity)
            ax.scatter(x_quality[idx], index, label='Qualidade', s=100, alpha=opacity)
            ax.scatter(x_pH[idx], index, label='pH', s=100, alpha=opacity)
            ax.scatter(x_sugar[idx], index, label='Açúcar residual', s=100, alpha=opacity)
            ax.scatter(x_sulfur[idx], index, label='Dióxido de enxofre total', s=100, alpha=opacity)
            ax.scatter(x_points[idx], index, label='Pontos', s=100, alpha=opacity)

            # Adicionar rótulo na direita
            ax.annotate('Preço médio', xy=(2, 'Preço médio'), xycoords='data', va='center')

        else:
            # Define a opacidade das demais vinícolas
            opacity = 0.2
            ax.scatter(x_price[idx], index, s=100, alpha=opacity)
            ax.scatter(x_quality[idx], index, s=100, alpha=opacity)
            ax.scatter(x_pH[idx], index, s=100, alpha=opacity)
            ax.scatter(x_sugar[idx], index, s=100, alpha=opacity)
            ax.scatter(x_sulfur[idx], index, s=100, alpha=opacity)
            ax.scatter(x_points[idx], index, s=100, alpha=opacity)

    ax.set_title('Preço médio, qualidade, pH, açúcar residual, dióxido de enxofre total e pontos por vinícula')
    ax.set_ylabel('Vinícola')
    ax.legend()

    # Salvar o gráfico em uma variável
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    plt.savefig(BASE_DIR / 'base' / 'static' / 'images' / 'grafico.png')


def filtros(dataframe, **kwargs):
    filtro: pd.core.frame.Dataframe = dataframe
    for k, v in kwargs.items():
        filtro = dataframe[k] == v
    return dataframe[filtro]


def conecta_db():
    conn_str = environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
    conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
    con = psycopg2.connect(host=conn_str_params['host'],
                           database=conn_str_params['dbname'],
                           user=conn_str_params['user'],
                           password=conn_str_params['password'])
    return con


def consultar_db(sql):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    con.close()
    return registros


def get_description(df_Winedata: pd.DataFrame, index):
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

    vinicula = filtros(df_Winedata, winery=vinicolas.get(index))
    return list(set(vinicula[vinicula.data_id == min(vinicula.data_id)].description))[0]

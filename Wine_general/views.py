from django.shortcuts import render
from .utils.utils import gera_grafico,get_description
import pandas as pd


# Create your views here.

def Wine_general(request, i=None):
    df_Winedata = pd.read_csv('base/static/WineData.csv', sep=';')
    if i is not None:
        gera_grafico(df_Winedata, i)
        description = get_description(df_Winedata, i)
        return render(
            request,
            'Wine_general/Wine_general.html',
            dict(i=i,
                 description=description)
        )
    return render(request, 'Wine_general/Wine_general.html')
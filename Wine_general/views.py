from django.shortcuts import render
from .utils.utils import gera_grafico, get_description, consultar_db
import pandas as pd


# Create your views here.
def Wine_general(request, i=None):
    wine = consultar_db('SELECT * FROM public."Wine_general_winedata" data, public ."Wine_general_winedetails" '
                        'detail where data.data_id = detail.detail_id')
    df_Winedata = pd.DataFrame(wine, columns=['data_id', 'country', 'description', 'designation', 'points', 'price',
                                              'winery', 'region_1', 'region_2', 'variety', 'province', 'detail_id',
                                              'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
                                              'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
                                              'ph', 'sulphates', 'alcohol', 'quality'])
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

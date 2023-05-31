from django.shortcuts import render
from .utils.utils import gera_grafico


# Create your views here.

def Wine_general(request, i):
    gera_grafico(i)
    return render(
        request,
        'Wine_general/Wine_general.html',
        dict(i=i)
    )

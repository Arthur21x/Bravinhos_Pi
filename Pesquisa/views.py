from django.shortcuts import render


# Create your views here.

def pesquisa(request):
    return render(request, 'Pesquisa/pesquisa.html')




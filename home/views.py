from django.shortcuts import render
# Create your views here.


def home(request):
    return render(
        request,
        'home/index.html',
        context=dict(lista=[c for c in range(1, 13)])
    )




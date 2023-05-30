from django.shortcuts import render


# Create your views here.

def Wine_general(request, i):
    return render(
        request,
        'Wine_general/Wine_general.html',
        dict(i=i)
    )

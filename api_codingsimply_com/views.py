from django.shortcuts import render


def index(request):
    context = {
        'apis': ['books'],
    }
    return render(request, 'index.html', context)

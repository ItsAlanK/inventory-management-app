from django.shortcuts import render


def index(request):
    """
    Return Homepage
    """
    return render(request, 'products/index.html')

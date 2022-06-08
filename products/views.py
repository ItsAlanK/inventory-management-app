from django.shortcuts import render
from .models import Product, Location, Inventory


def index(request):
    """
    Return Homepage containing list of products
    """

    products = Product.objects.all()

    context = {
        'products':products,
    }

    return render(request, 'products/index.html', context)

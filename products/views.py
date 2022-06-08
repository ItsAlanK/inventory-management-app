from django.shortcuts import render
from .models import Product, Location, Inventory


def index(request):
    """
    Return Homepage containing list of products
    """

    products = Product.objects.all()
    locations = Location.objects.all()
    inventory = Inventory.objects.all()

    context = {
        'products': products,
        'locations': locations,
        'inventory': inventory,
    }

    return render(request, 'products/index.html', context)

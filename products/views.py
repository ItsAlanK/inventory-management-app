from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.forms import formset_factory
from .models import Product, Location, Inventory
from .forms import ProductForm, InventoryForm, LocationForm


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


def add_product(request):
    """ Add a product to list """

    if request.method == 'POST':
        productform = ProductForm(request.POST)
        inventoryform = InventoryForm(request.POST)
        if productform.is_valid() and inventoryform.is_valid():
            product = productform.save()
            inventory = inventoryform.save(commit=False)
            inventory.product = product
            inventory.save()
            return redirect(
                reverse('home'))
        else:
            print('Error')
    else:
        productform = ProductForm()
        inventoryform = InventoryForm()

    template = 'products/add-product.html'
    context = {
        'productform': productform,
        'inventoryform': inventoryform,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """
    Edit product details and inventory information
    """
    product = get_object_or_404(Product, pk=product_id)
    product_form = ProductForm(instance=product)

    inventory = Inventory.objects.all()
    product_inventory = []

    for i in inventory:
        if i.product == product:
            product_inventory.append(i)

    template = 'products/edit-product.html'

    context={
            'product_form': product_form,
            'product': product,
            'product_inventory': product_inventory,
            }

    return render(request, template, context)


def add_location(request):
    """ Add a location """

    if request.method == 'POST':
        locationform = LocationForm(request.POST)
        if locationform.is_valid():
            location = locationform.save()
            return redirect(
                reverse('home'))
        else:
            print('Error saving location')
    else:
        locationform = LocationForm()

    template = 'products/add-location.html'
    context = {
        'locationform': locationform,
    }

    return render(request, template, context)


def locations(request):
    """
    View to handle displaying location list
    """

    locations = Location.objects.all()
    inventory = Inventory.objects.all()

    context = {
        'locations': locations,
        'inventory': inventory,
    }

    return render(request, 'products/locations.html', context)


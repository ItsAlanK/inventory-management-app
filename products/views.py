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


# Product Management
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
            print('Product Added successfully')
        else:
            print('Error product not added')
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

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            print('product updated successfully')
            return redirect(reverse('home'))


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


def delete_product(request, product_id):
    """ Delete a product """

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    print(f"Product: {product} successfully deleted")
    return redirect(reverse('home'))


# Inventory Management
def add_inventory(request, product_id):
    """ Add a product inventory to location """

    product = get_object_or_404(Product, pk=product_id)
    inventory_list = Inventory.objects.all()
 
    if request.method == 'POST':
        inventoryform = InventoryForm(request.POST)
        if inventoryform.is_valid():
            inventory = inventoryform.save(commit=False)
            already_exists = False

            for i in inventory_list:
                if inventory.location == i.location and i.product == product:
                    already_exists = True
                    i.quantity += inventory.quantity
                    i.save()
                    return redirect(reverse('home'))
            if not already_exists:
                inventory.product = product
                inventory.save()
                return redirect(
                    reverse('home'))
                print('Product Added location successfully')
        else:
            print('Error product not added')
    else:
        inventoryform = InventoryForm()

    template = 'products/add-inventory.html'
    context = {
        'product': product,
        'inventoryform': inventoryform,
    }

    return render(request, template, context)


# Location Management
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


def edit_location(request, location_id):
    """
    Edit location details
    """
    location = get_object_or_404(Location, pk=location_id)
    location_form = LocationForm(instance=location)

    if request.method == 'POST':
        location_form = LocationForm(request.POST, request.FILES, instance=location)
        if location_form.is_valid():
            location_form.save()
            print('location updated successfully')
            return redirect(reverse('locations'))

    template = 'products/edit-location.html'

    context={
            'location_form': location_form,
            'location': location,
            }

    return render(request, template, context)


def delete_location(request, location_id):
    """ Delete a location """

    location = get_object_or_404(Location, pk=location_id)
    location.delete()
    print(f"Product: {location} successfully deleted")
    return redirect(reverse('home'))


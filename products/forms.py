from django import forms
from .models import Product, Inventory, Location


class ProductForm(forms.ModelForm):
    """ Form for managing products from front end. """

    class Meta:
        model = Product
        fields = '__all__'

class InventoryForm(forms.ModelForm):
    """ Form for managing product inventory from front end. """

    class Meta:
        """ Set fields for inventory form """
        model = Inventory
        fields = ('quantity', 'location',)


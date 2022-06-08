from django.db import models


class Product(models.Model):
    """
    Model for each products details
    """
    SKU = models.IntegerField(default=0)
    name = models.CharField(max_length=254)
    weight = models.IntegerField(default=0)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    """
    Model for each locations details
    """
    name = models.CharField(max_length=254)
    address_line_1 = models.CharField(max_length=254)
    address_line_2 = models.CharField(max_length=254, null=True, blank=True)
    address_line_3 = models.CharField(max_length=254, null=True, blank=True)
    county = models.CharField(max_length=254, default='county')
    postcode = models.CharField(max_length=254, default='postcode')
    country = models.CharField(max_length=254, default='country')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    """
    Model which tracks inventory for each product
    and assigns its location.
    """

    class Meta:
        """ Adjust plural of model name in admin """
        verbose_name_plural = 'Inventory'

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    location = models.ForeignKey('Location', on_delete=models.PROTECT)

    def __str__(self):
        return self.product.name

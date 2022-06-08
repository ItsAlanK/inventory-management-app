from django.contrib import admin
from .models import Product, Location, Inventory


class InventoryAdminInline(admin.TabularInline):

    model = Inventory

    list_display = (
        'product',
        'quantity',
        'location'
    )


class ProductAdmin(admin.ModelAdmin):

    inlines = (InventoryAdminInline,)

    list_display = (
        'name',
        'SKU',
        'weight',
        'value',
        'notes'
    )

    ordering = ('name',)


class LocationAdmin(admin.ModelAdmin):

    inlines = (InventoryAdminInline,)

    list_display = (
        'name',
        'address_line_1',
        'address_line_2',
        'address_line_3',
        'county',
        'postcode',
        'country',
    )

    ordering = ('name',)


class InventoryAdmin(admin.ModelAdmin):

    model = Inventory

    list_display = (
        'product',
        'quantity',
        'location'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Inventory, InventoryAdmin)

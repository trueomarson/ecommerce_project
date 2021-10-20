from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecyficationValue,
    ProductType,
)

admin.site.register(Category, MPTTModelAdmin)

class ProductSpecialisationInline(admin.TabularInline):
    model = ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecialisationInline,
    ]

class ProductImageInline(admin.TabularInline):





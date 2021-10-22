from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
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
    model = ProductImage

class ProductSpecificationonValueInline(admin.TabularInline):
    model = ProductSpecificationonValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationonValueInline,
        ProductImageInline,
    ]








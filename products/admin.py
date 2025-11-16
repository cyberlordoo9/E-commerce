from django.contrib import admin
from .models import Product, Category, Brand, ProductVariant, ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'stock', 'is_active')
    list_filter = ('brand', 'category', 'is_active')
    search_fields = ('name', 'slug', 'sku')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductVariant)
admin.site.register(ProductImage)

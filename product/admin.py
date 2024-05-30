from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    # Setting this will help to delete files when deleted via the admin
    def delete_model(self, request, obj):
        if obj.image:
            obj.image.delete()
        obj.delete()

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'category', 'status')
    search_fields = ('name', 'sku')
    list_filter = ('category', 'status')
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
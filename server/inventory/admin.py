from django.contrib import admin
from .models import Category, NFC, Product, ProductImage

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def get_readonly_fields(self, request, obj=None):
        return ['id'] if obj else []

admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(NFC)
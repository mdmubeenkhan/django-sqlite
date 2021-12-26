from django.contrib import admin
from shopping.models import Items

# Register your models here.
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']

admin.site.register(Items, ItemsAdmin)
from django.contrib import admin
from .models import Category ,Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update',) # tuple is faster than lists
    list_filter = ('name','create','update',)
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','amount','unit_price','discount','total_price','information','available','create','update',) # tuple is faster than lists
    #list_filter = ('name','amount','unit_price','discount','total_price','information','create','update',)
admin.site.register(Product,ProductAdmin)
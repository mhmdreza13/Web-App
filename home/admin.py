from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update',) # tuple is faster than lists
    list_filter = ('name','create','update',)
admin.site.register(Category,CategoryAdmin)
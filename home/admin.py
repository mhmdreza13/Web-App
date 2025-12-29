from django.contrib import admin
from .models import Category ,Product , Variants ,Color ,Size
# Register your models here.

class ProductsVariantInlines (admin.TabularInline):
    model = Variants
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update','sub_category') # tuple is faster than lists
    list_filter = ('name','create','update',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','amount','unit_price','discount','total_price','information','available','create','update',) # tuple is faster than lists
    #list_filter = ('name','amount','unit_price','discount','total_price','information','create','update',)
    list_editable = ('amount','unit_price','discount','available',)
    raw_id_fields = ('category',)
    inlines = [ProductsVariantInlines]
    


admin.site.register(Product,ProductAdmin)
admin.site.register(Variants)
admin.site.register(Color)
admin.site.register(Size)
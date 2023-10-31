from django.contrib import admin
from online.models import Employer, Store, Product

# Register your models here.
# admin.site.register(Employer)
# admin.site.register(Store)
# admin.site.register(Product)

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')
    
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'employer')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_store')

admin.site.register(Employer, EmployerAdmin)
# @admin.register(Product) === admin.site.register(Product, ProductAdmin)

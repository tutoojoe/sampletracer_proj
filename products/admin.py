from django.contrib import admin
from products.models import Season, ProductGroup, Style, Accessories, Processes

# Register your models here.


admin.site.register(Season)
admin.site.register(ProductGroup)
admin.site.register(Style)
admin.site.register(Accessories)
admin.site.register(Processes)

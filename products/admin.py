from django.contrib import admin
from products.models import MeasurementChart, Measurements, Season, ProductGroup, Style, Accessories, Processes

# Register your models here.


admin.site.register(Season)
admin.site.register(ProductGroup)
admin.site.register(Style)
admin.site.register(Accessories)
admin.site.register(Processes)
admin.site.register(MeasurementChart)
admin.site.register(Measurements)

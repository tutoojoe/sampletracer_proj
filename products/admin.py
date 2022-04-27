from django.contrib import admin
from products.models import MeasurementChart, Measurements, Season, ProductGroup, Style, Accessories, Processes

# Register your models here.


class MeasurementsInline(admin.TabularInline):
    model = Measurements
    extra = 1


class MeasurementChartAdmin(admin.ModelAdmin):
    inlines = [MeasurementsInline]


admin.site.register(Season)
admin.site.register(ProductGroup)
admin.site.register(Style)
admin.site.register(Accessories)
admin.site.register(Processes)
admin.site.register(MeasurementChart, MeasurementChartAdmin)
admin.site.register(Measurements)

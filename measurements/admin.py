from django.contrib import admin
from .models import MeasurementChart, Measurements

# Register your models here.


class MeasurementsInline(admin.TabularInline):
    model = Measurements
    extra = 1


class MeasurementChartAdmin(admin.ModelAdmin):
    inlines = [MeasurementsInline]


admin.site.register(MeasurementChart, MeasurementChartAdmin)
admin.site.register(Measurements)

from django.urls import path
from .views import MeasurementChartListCreateView, MeasurementsCreateView

urlpatterns = [
    path('', MeasurementChartListCreateView.as_view(),
         name="measurements"),
    path('add/', MeasurementsCreateView.as_view(),
         name="add_measurements"),
]

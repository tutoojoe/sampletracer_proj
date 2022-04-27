
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StylesListView.as_view(), name='styles_list'),
    path('product_groups/', views.ProductGroupListCreateAPIView.as_view(),
         name='product_group_list'),
    path('measurements/', views.MeasurementListAPIView.as_view(), name="measurements"),
    path('measurements/detail', views.MeasurementItemsListCreateAPIView.as_view(),
         name="measurement_detail"),

]

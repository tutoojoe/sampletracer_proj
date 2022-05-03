
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StylesListView.as_view(), name='styles_list'),
    path('add_product/', views.StylesCreateView.as_view(), name='add_styles'),
    path('product_groups/', views.ProductGroupListCreateAPIView.as_view(),
         name='product_group_list'),
    path('measurements/', views.MeasurementChartListCreateView.as_view(),
         name="measurements"),
    path('measurements/add', views.MeasurementsCreateView.as_view(),
         name="add_measurements"),
    path('colors/', views.ColorsListCreateView.as_view(), name='colors'),
    path('colors/<int:pk>/', views.ColorsDetailUpdateDeleteView.as_view(),
         name='colors_detail'),
    path('stylecombo/', views.StyleComboListCreateView.as_view(), name='stylecombos'),
    path('stylecombo/<int:pk>/',
         views.StyleComboDetailUpdateDeleteView.as_view(), name='stylecombo_detail'),


]

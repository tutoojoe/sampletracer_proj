
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StylesListView.as_view(), name='styles_list'),
    path('<int:pk>', views.StyleDetailEditUpdateDeleteView.as_view(),
         name="style_details"),
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

    path('seasons/', views.SeasonListCreateView.as_view(), name='seasons'),
    path('seasons/<int:pk>/',
         views.SeasonDetailEditDeleteView.as_view(), name='season_detail'),
    path('accessories/',
         views.AccessoriesListCreateView.as_view(), name="accessories"),
    path('accessories/<int:pk>/',
         views.AccessoriesDetailEditDeleteView.as_view(), name="accessories_detail"),
    path('processes/',
         views.ProcessesListCreateView.as_view(), name="processes"),
    path('processes/<int:pk>/',
         views.ProcessDetailEditDeleteView.as_view(), name="processes_detail"),


]

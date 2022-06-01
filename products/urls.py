
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StylesListView.as_view(), name='styles_list'),
    path('<int:pk>', views.StyleDetailEditUpdateDeleteView.as_view(),
         name="style_details"),
    path('add_product/', views.StylesCreateView.as_view(), name='add_styles'),



    #     path('seasons/', views.SeasonListCreateView.as_view(), name='seasons'),
    #     path('seasons/<int:pk>/',
    #          views.SeasonDetailEditDeleteView.as_view(), name='season_detail'),
    #     path('accessories/',
    #          views.AccessoriesListCreateView.as_view(), name="accessories"),
    #     path('accessories/<int:pk>/',
    #          views.AccessoriesDetailEditDeleteView.as_view(), name="accessories_detail"),



]

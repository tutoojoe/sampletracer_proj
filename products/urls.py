
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StylesListView.as_view(), name='styles_list'),
    path('product_groups/', views.ProductGroupListCreateAPIView.as_view(),
         name='product_group_list')
]

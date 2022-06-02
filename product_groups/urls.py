from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductGroupListCreateAPIView.as_view(),
         name='product_groups'),
    path('<int:pk>/', views.ProductGroupDetailUpdateDeleteView.as_view(),
         name='product_group_detail')
]

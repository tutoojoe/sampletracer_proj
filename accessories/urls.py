from django.urls import path
from .views import AccessoriesListCreateView, AccessoriesDetailEditDeleteView

urlpatterns = [
    path('', AccessoriesListCreateView.as_view(), name='accessories'),
    path('<int:pk>/', AccessoriesDetailEditDeleteView.as_view(),
         name='accessories_detail'),
]

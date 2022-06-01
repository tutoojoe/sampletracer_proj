from django.urls import path, include
from .views import ColorsListCreateView, ColorsDetailUpdateDeleteView

urlpatterns = [
    path('', ColorsListCreateView.as_view(), name='colors'),
    path('<int:pk>/', ColorsDetailUpdateDeleteView.as_view(),
         name='colors_detail'),
]

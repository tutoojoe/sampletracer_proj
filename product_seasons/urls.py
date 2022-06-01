from django.urls import path
from .views import SeasonListCreateView, SeasonDetailEditDeleteView

urlpatterns = [
    path('', SeasonListCreateView.as_view(), name='seasons'),
    path('<int:pk>/',
         SeasonDetailEditDeleteView.as_view(), name='season_detail'),
]

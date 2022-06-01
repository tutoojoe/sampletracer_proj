
from django.urls import path, include
from .views import StyleComboDetailUpdateDeleteView, StyleComboListCreateView

urlpatterns = [
    path('', StyleComboListCreateView.as_view(), name='stylecombos'),
    path('<int:pk>/',
         StyleComboDetailUpdateDeleteView.as_view(), name='stylecombo_detail'),

]

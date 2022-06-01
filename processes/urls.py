from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.ProcessesListCreateView.as_view(), name="processes"),
    path('<int:pk>/',
         views.ProcessDetailEditDeleteView.as_view(), name="processes_detail"),
]

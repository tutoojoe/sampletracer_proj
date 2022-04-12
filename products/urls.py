
from django.urls import path, include
from products import views

urlpatterns = [
    path('', views.StylesListView.as_view(), name='styles_list'),
]

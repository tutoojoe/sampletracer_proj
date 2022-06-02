
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StylesListView.as_view(), name='styles_list'),
    path('<int:pk>', views.StyleDetailEditUpdateDeleteView.as_view(),
         name="style_details"),
    path('add_product/', views.StylesCreateView.as_view(), name='add_styles'),
]

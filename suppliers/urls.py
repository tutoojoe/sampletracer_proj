from django.urls import path, include
from suppliers.views import SupplierListCreateAPIView, SupplierRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', SupplierListCreateAPIView.as_view(), name="supplier_list"),
    path('supplierdetail/<int:pk>', SupplierRetrieveUpdateDestroyAPIView.as_view(),
         name="supplierdetail"),


]

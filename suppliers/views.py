from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from suppliers.models import Suppliers
from suppliers.serializers import SupplierSerializer

# Create your views here.


class SupplierListCreateAPIView(ListCreateAPIView):
    """_Supplier Listing/Creation_
    Args:
        ListCreateAPIView (POST): _listing all the styles_
    """

    queryset = Suppliers.objects.all()
    permission_classes = []
    serializer_class = SupplierSerializer


class SupplierRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Suppliers View, Edit, Update or delete

    Args:
        RetrieveUpdateDestroyAPIView (_pk_): _primarykey of supplier_
    """
    permission_classes = []
    serializer_class = SupplierSerializer

    def get_queryset(self):
        return Suppliers.objects.all()

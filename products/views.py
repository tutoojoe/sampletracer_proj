from django.shortcuts import render
from products.models import Style
from products.serializers import StyleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404


from products.serializers import StyleDetailedSerializer, StyleCreateSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from products.models import ProductGroup
from products.serializers import ProductGroupSerializer


# Create your views here.


class StylesListView(generics.ListCreateAPIView):
    """
    Lists out all the styles 
    """
    queryset = Style.objects.all()
    serializer_class = StyleCreateSerializer

    # class StylesListView(APIView):
    #     def get(self, request, format=None):
    #         styles = Style.objects.all()
    #         serializer = StyleSerializer(styles, many=True)
    #         return Response(serializer.data)

    #     def post(self, request, format=None):

    #         serializer = StyleSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductGroupListCreateAPIView(generics.ListCreateAPIView):
    """
    View to List all product groups in the system
    # """
    serializer_class = ProductGroupSerializer

    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """ Returns a list of all the product groups"""
        product_groups = ProductGroup.objects.all()
        serializer = self.serializer_class(product_groups, many=True)
        return Response(serializer.data)

    def get(self, request, format=None):
        """ Returns a list of all the product groups"""
        product_groups = ProductGroup.objects.all()
        serializer = self.serializer_class(product_groups, many=True)
        return Response(serializer.data)

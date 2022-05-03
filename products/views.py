from django.shortcuts import render
from products.models import MeasurementChart, Style, Measurements, ProductGroup, Colors, StyleCombo
from products.serializers import StyleCreateSerializer, StyleDetailedSerializer, MeasurementItemSerializer, ProductGroupSerializer, MeasurementSerializer, StyleSerializer, ColorSerializer, StyleComboSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class StylesListView(generics.ListAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class StylesCreateView(generics.CreateAPIView):
    """
    Lists out all the styles 
    """
    serializer_class = StyleCreateSerializer
    queryset = Style.objects.all()


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


class MeasurementChartListCreateView(generics.ListCreateAPIView):
    serializer_class = MeasurementSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = MeasurementChart.objects.all()
        return queryset


class MeasurementsCreateView(generics.CreateAPIView):
    serializer_class = MeasurementItemSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Measurements.objects.all()
        return queryset


class ColorsListCreateView(generics.ListCreateAPIView):
    serializer_class = ColorSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Colors.objects.all()
        return queryset


class ColorsDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ColorSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Colors.objects.all()
        return queryset


class StyleComboListCreateView(generics.ListCreateAPIView):
    serializer_class = StyleComboSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = StyleCombo.objects.all()
        return queryset


class StyleComboDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StyleComboSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = StyleCombo.objects.all()
        return queryset

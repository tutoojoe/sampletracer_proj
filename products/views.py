from django.shortcuts import render
from products.models import Accessories, Processes, MeasurementChart, Style, Measurements, ProductGroup, Colors, Season, StyleCombo
from products.serializers import AccessoriesSerializer, ProcessesSerializer, SeasonSerializer, StyleCreateSerializer, StyleDetailedSerializer, MeasurementItemSerializer, ProductGroupSerializer, MeasurementSerializer, StyleSerializer, ColorSerializer, StyleComboSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.

class ProcessesListCreateView(generics.ListCreateAPIView):
    """
    Lists out the processes or Create a Process in a style"""
    serializer_class = ProcessesSerializer
    queryset = Processes.objects.all()


class ProcessDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Process Retrievd, Update, Edit or Delete view

    Args:
        generics (pk): retrieves the process object related to the given id
    """
    serializer_class = ProcessesSerializer
    queryset = Processes.objects.all()


class AccessoriesListCreateView(generics.ListCreateAPIView):
    """
    GET> Lists out all the accessories\n
    POST> Create an accessories object
    """
    serializer_class = AccessoriesSerializer
    queryset = Accessories.objects.all()


class AccessoriesDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Accessory object based on pk/id \n
    GET: retrieves object related to the given id \n
    PUT: Edits the objects related to the given id \n
    PATCH: Update a part of the object related to the given id \n
    DELETE: Deletes the particular object

    Args:
        generics (pk): pk/id of the object
    """
    serializer_class = AccessoriesSerializer
    queryset = Accessories.objects.all()


class StylesListView(generics.ListAPIView):
    """
    Returns a list of all the styls
    """
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class SeasonListCreateView(generics.ListCreateAPIView):
    """
    Generates a list of the seasons or create a new season.
    """
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SeasonDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generates a list of the seasons or create a new season.
    """
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class StylesCreateView(generics.CreateAPIView):
    """
    Create a new Style (Product) 
    """
    serializer_class = StyleCreateSerializer
    queryset = Style.objects.all()


class StyleDetailEditUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Create a new Style (Product) 
    """
    serializer_class = StyleSerializer
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

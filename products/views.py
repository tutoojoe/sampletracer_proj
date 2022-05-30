
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from .models import (Accessories, Processes, MeasurementChart,
                     Style, Measurements, ProductGroup, Colors,
                     Season, StyleCombo)
from .serializers import (AccessoriesSerializer, ProcessesSerializer,
                          SeasonSerializer, StyleCreateSerializer,
                          StyleDetailedSerializer,
                          MeasurementItemSerializer,
                          ProductGroupSerializer,
                          MeasurementSerializer,
                          StyleSerializer, ColorSerializer,
                          StyleComboSerializer)


from socketio_server import sio


# Create your views here.
from rest_framework import mixins
from rest_framework import generics


class ProcessesListCreateView(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              generics.GenericAPIView):

    # class ProcessesListCreateView(APIView):
    # class ProcessesListCreateView(generics.ListCreateAPIView):
    """
    Lists out the processes or Create a Process in a style"""
    serializer_class = ProcessesSerializer
    queryset = Processes.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get(self, request, format=None):
    #     serializer = ProcessesSerializer(style_processes, many=True)
    #     return Response(serializer.data)

    # @sio.event
    # def post(self, request, format=None):
    #     serializer = ProcessesSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         sio.emit('process_added', {'msg': 'process_added'})
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProcessDetailEditDeleteView(APIView):
    # class ProcessDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Process Retrievd, Update, Edit or Delete view

    Args:
        generics (pk): retrieves the process object related to the given id
    """
    # serializer_class = ProcessesSerializer
    # queryset = Processes.objects.all()

    def get_object(self, pk):
        try:
            return Processes.objects.get(pk=pk)
        except Processes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        process = self.get_object(pk)
        serializer = ProcessesSerializer(process)
        return Response(serializer.data)

    @sio.event
    def put(self, request, pk, format=None):
        process = self.get_object(pk)
        serializer = ProcessesSerializer(process, data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('process_edited', {'data': 'Process Edited'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @sio.event
    def delete(self, request, pk, format=None):
        process = self.get_object(pk)
        process.delete()
        sio.emit('process_deleted', {'data': 'Process Deleted'})
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccessoriesListCreateView(APIView):
    # class AccessoriesListCreateView(generics.ListCreateAPIView):

    """
    GET> Lists out all the accessories\n
    POST> Create an accessories object
    """
    # serializer_class = AccessoriesSerializer
    # queryset = Accessories.objects.all()

    def get(self, request, format=None):
        accessories = Accessories.objects.all()
        serializer = AccessoriesSerializer(accessories, many=True)
        return Response(serializer.data)

    @sio.event
    def post(self, request, format=None):
        serializer = AccessoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('accessory_created', {'msg': 'New accessory created'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccessoriesDetailEditDeleteView(APIView):
    # class AccessoriesDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Accessory object based on pk/id \n
    GET: retrieves object related to the given id \n
    PUT: Edits the objects related to the given id \n
    PATCH: Update a part of the object related to the given id \n
    DELETE: Deletes the particular object

    Args:
        generics (pk): pk/id of the object
    """
    # serializer_class = AccessoriesSerializer
    # queryset = Accessories.objects.all()

    def get_object(self, pk):
        try:
            return Accessories.objects.get(pk=pk)
        except Accessories.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        accessory = self.get_object(pk)
        serializer = AccessoriesSerializer(accessory)
        return Response(serializer.data)

    @sio.event
    def put(self, request, pk, format=None):
        accessory = self.get_object(pk)
        serializer = AccessoriesSerializer(accessory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('accessory_edited', {'data': 'Accessory Edited'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @sio.event
    def delete(self, request, pk, format=None):
        accessory = self.get_object(pk)
        accessory.delete()
        sio.emit('Accessory_deleted', {'data': 'Accessory Deleted'})
        return Response(status=status.HTTP_204_NO_CONTENT)


class StylesListView(generics.ListAPIView):
    """
    Returns a list of all the styls
    """
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class SeasonListCreateView(APIView):
    # class SeasonListCreateView(generics.ListCreateAPIView):
    """
    Generates a list of the seasons or create a new season.
    """
    # queryset = Season.objects.all()
    # serializer_class = SeasonSerializer

    def get(self, request, format=None):
        seasons = Season.objects.all()
        serializer = SeasonSerializer(seasons, many=True)
        return Response(serializer.data)

    @sio.event
    def post(self, request, format=None):
        serializer = SeasonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('season_created', {'msg': 'New Season created'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeasonDetailEditDeleteView(APIView):
    # class SeasonDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generates a list of the seasons or create a new season.
    """
    # queryset = Season.objects.all()
    # serializer_class = SeasonSerializer

    def get_object(self, pk):
        try:
            return Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        season = self.get_object(pk)
        serializer = SeasonSerializer(season)
        return Response(serializer.data)

    @sio.event
    def put(self, request, pk, format=None):
        season = self.get_object(pk)
        serializer = SeasonSerializer(season, data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('season_edited', {'data': 'Season Edited'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @sio.event
    def delete(self, request, pk, format=None):
        season = self.get_object(pk)
        season.delete()
        sio.emit('season_deleted', {'data': 'Season Deleted'})
        return Response(status=status.HTTP_204_NO_CONTENT)


class StylesCreateView(APIView):

    @sio.event
    def post(self, request, format=None):
        serializer = StyleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('product_added', {
                     'msg': 'New product added'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class StylesCreateView(generics.CreateAPIView):
#     """
#     Create a new Style (Product)
#     """
#     serializer_class = StyleCreateSerializer
#     queryset = Style.objects.all()


class StyleDetailEditUpdateDeleteView(APIView):
    # class StyleDetailEditUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Create a new Style (Product)
    """
    # serializer_class = StyleSerializer
    # queryset = Style.objects.all()

    def get_object(self, pk):
        try:
            return Style.objects.get(pk=pk)
        except Style.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        style = self.get_object(pk)
        serializer = StyleSerializer(style)
        return Response(serializer.data)

    @sio.event
    def put(self, request, pk, format=None):
        style = self.get_object(pk)
        serializer = StyleSerializer(style, data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('style_edited', {'data': 'Style Edited'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @sio.event
    def delete(self, request, pk, format=None):
        style = self.get_object(pk)
        style.delete()
        sio.emit('style_deleted', {'data': 'Style Deleted'})
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductGroupListCreateAPIView(APIView):
class ProductGroupListCreateAPIView(mixins.ListModelMixin,
                                    mixins.CreateModelMixin,
                                    generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        sio.emit('product_group_added', {
            'msg': 'product group added'})
        return self.create(request, *args, **kwargs)

#    def get(self, request, format=None):
#         product_groups = ProductGroup.objects.all()
#         serializer = ProductGroupSerializer(product_groups, many=True)
#         return Response(serializer.data)

#     # @sio.event
#     def post(self, request, format=None):
#         serializer = ProductGroupSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             sio.emit('product_group_added', {
#                      'msg': 'product group added', 'group_name': serializer.data['product_group']})
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductGroupListCreateAPIView(generics.ListCreateAPIView):
#     """
#     View to List all product groups in the system
#     # """
#     serializer_class = ProductGroupSerializer

#     # permission_classes = [IsAuthenticated]

#     sio.emit("my_response", {"data": "product group altered"})

#     def get(self, request, format=None):
#         """ Returns a list of all the product groups"""

#         product_groups = ProductGroup.objects.all()
#         serializer = self.serializer_class(product_groups, many=True)
#         return Response(serializer.data)

    # def get(self, request, format=None):
    #     """ Returns a list of all the product groups"""
    #     product_groups = ProductGroup.objects.all()
    #     serializer = self.serializer_class(product_groups, many=True)
    #     return Response(serializer.data)


class MeasurementChartListCreateView(APIView):
    # class MeasurementChartListCreateView(generics.ListCreateAPIView):
    # serializer_class = MeasurementSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = MeasurementChart.objects.all()
    #     return queryset
    def get(self, request, format=None):
        product_groups = MeasurementChart.objects.all()
        serializer = MeasurementSerializer(product_groups, many=True)
        return Response(serializer.data)

    @sio.event
    def post(self, request, format=None):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('mc_created', {'msg': 'New MC created'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementsCreateView(generics.CreateAPIView):
    serializer_class = MeasurementItemSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Measurements.objects.all()
        return queryset


class ColorsListCreateView(APIView):
    # class ColorsListCreateView(generics.ListCreateAPIView):
    # serializer_class = ColorSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = Colors.objects.all()
    #     return queryset

    def get(self, request, format=None):
        colors = Colors.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)

    @sio.event
    def post(self, request, format=None):
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('color_created', {'msg': 'New color created'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorsDetailUpdateDeleteView(APIView):

    # class ColorsDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # serializer_class = ColorSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Colors.objects.get(pk=pk)
        except Colors.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        color = self.get_object(pk)
        serializer = ColorSerializer(color)
        return Response(serializer.data)

    @sio.event
    def put(self, request, pk, format=None):
        color = self.get_object(pk)
        serializer = ColorSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('color_edited', {'data': 'Color Edited'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @sio.event
    def delete(self, request, pk, format=None):
        color = self.get_object(pk)
        color.delete()
        sio.emit('color_deleted', {'data': 'Color Deleted'})
        return Response(status=status.HTTP_204_NO_CONTENT)


class StyleComboListCreateView(APIView):
    # class StyleComboListCreateView(generics.ListCreateAPIView):
    # serializer_class = StyleComboSerializer
    # # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = StyleCombo.objects.all()
    #     return queryset
    def get(self, request, format=None):
        combos = StyleCombo.objects.all()
        serializer = StyleComboSerializer(combos, many=True)
        return Response(serializer.data)

    @sio.event
    def post(self, request, format=None):
        serializer = StyleComboSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('stylecombo_created', {'msg': 'New Style combo created'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StyleComboDetailUpdateDeleteView(APIView):
    # class StyleComboDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # serializer_class = StyleComboSerializer
    # # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = StyleCombo.objects.all()
    #     return queryset

    def get_object(self, pk):
        try:
            return StyleCombo.objects.get(pk=pk)
        except StyleCombo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stylecombo = self.get_object(pk)
        serializer = StyleComboSerializer(stylecombo)
        return Response(serializer.data)

    @sio.event
    def put(self, request, pk, format=None):
        stylecombo = self.get_object(pk)
        serializer = StyleComboSerializer(stylecombo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            sio.emit('stylecombo_edited', {'data': 'Stylecombo Edited'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @sio.event
    def delete(self, request, pk, format=None):
        stylecombo = self.get_object(pk)
        stylecombo.delete()
        sio.emit('stylecombo_deleted', {'data': 'Stylecombo Deleted'})
        return Response(status=status.HTTP_204_NO_CONTENT)

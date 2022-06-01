from django.shortcuts import render
from rest_framework import mixins, generics
from socketio_server import sio
from .models import Measurements, MeasurementChart
from .serializers import MeasurementSerializer, MeasurementItemSerializer

# Create your views here.


# class MeasurementChartListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

#     serializer_class = MeasurementSerializer
#     queryset = MeasurementChart.objects.all()

#     def get(self, request, *args, **kwargs):
#         """ Returns a list of accessories"""
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         """ Create a new accessory"""
#         sio.emit('measurementchart', {'msg': 'process_added'})
#         return self.create(request, *args, **kwargs)


class MeasurementChartListCreateView(mixins.ListModelMixin,
                                     mixins.CreateModelMixin,
                                     generics.GenericAPIView):

    queryset = MeasurementChart.objects.all()
    serializer_class = MeasurementSerializer

    def get(self, request, *args, **kwargs):
        """Lists out all the measurement charts"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Creates a new Measurement Chart"""
        sio.emit("measurement_chart", {"msg": "new measurement chart added"})
        return self.create(request, *args, **kwargs)


class MeasurementsCreateView(generics.CreateAPIView):
    serializer_class = MeasurementItemSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Measurements.objects.all()
        return queryset

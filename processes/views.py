from django.shortcuts import render
from rest_framework import generics, mixins
from socketio_server import sio
from .models import Processes
from .serializers import ProcessesSerializer


# Create your views here.


class ProcessesListCreateView(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              generics.GenericAPIView):

    serializer_class = ProcessesSerializer
    queryset = Processes.objects.all()

    def get(self, request, *args, **kwargs):
        """ Lists out the processes or Create a Process in a style"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Creates a new Process"""
        sio.emit('process', {'msg': 'process_added'})
        return self.create(request, *args, **kwargs)


class ProcessDetailEditDeleteView(mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  generics.GenericAPIView):

    queryset = Processes.objects.all()
    serializer_class = ProcessesSerializer

    def get(self, request, *args, **kwargs):
        """Retrieves a single object matching the given pk"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates an object based on the PK"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete an object based on the pk"""
        return self.destroy(request, *args, **kwargs)

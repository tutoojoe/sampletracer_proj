from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from socketio_server import sio
from .models import Colors
from .serializers import ColorSerializer

# Create your views here.


class ColorsListCreateView(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    queryset = Colors.objects.all()
    serializer_class = ColorSerializer

    def get(self, request, *args, **kwargs):
        """ List out the list of Colors"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Creates a new Color"""
        sio.emit("color", {"msg": "new color added"})
        return self.create(request, *args, **kwargs)


class ColorsDetailUpdateDeleteView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   generics.GenericAPIView):
    queryset = Colors.objects.all()
    serializer_class = ColorSerializer

    def get(self, request, *args, **kwargs):
        """Returns a single object ('Color')"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """ Update a unique object(color) based on pk"""
        sio.emit('color', {"msg": "color updated"})
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ Deletes a unique color object based on the given pk(id)"""
        sio.emit("color", {"msg": "color deleted"})
        return self.destroy(request, *args, **kwargs)

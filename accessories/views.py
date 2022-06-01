from django.shortcuts import render
from rest_framework import mixins, generics
from socketio_server import sio
from .models import Accessories
from .serializers import AccessoriesSerializer

# Create your views here.


class AccessoriesListCreateView(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                generics.GenericAPIView):
    serializer_class = AccessoriesSerializer
    queryset = Accessories.objects.all()

    def get(self, request, *args, **kwargs):
        """ Returns a list of accessories"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Create a new accessory"""
        sio.emit('accessory_added', {'msg': 'process_added'})
        return self.create(request, *args, **kwargs)


class AccessoriesDetailEditDeleteView(mixins.RetrieveModelMixin,
                                      mixins.UpdateModelMixin,
                                      mixins.DestroyModelMixin,
                                      generics.GenericAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer

    def get(self, request, *args, **kwargs):
        """Returns a single object based on the 'pk'
        """

        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Edits/Update a single object based on the 'pk'.
        """
        sio.emit("accessory", {"msg": "accessory edited"})
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Deletes a single object based on the 'pk'.
        """
        sio.emit("accessory", {"msg": "accessory deleted"})

        return self.destroy(request, *args, **kwargs)

from django.shortcuts import render
from rest_framework import mixins, generics
from socketio_server import sio
from .serializers import SeasonSerializer
from .models import Season
# Create your views here.


class SeasonListCreateView(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()

    def get(self, request, *args, **kwargs):
        """ Returns a list of all seasons"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Create a new Season"""
        sio.emit('season', {'msg': 'season created'})
        return self.create(request, *args, **kwargs)


class SeasonDetailEditDeleteView(mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 generics.GenericAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    def get(self, request, *args, **kwargs):
        """ Returns a single Season object"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """ Update a 'Season' object based on the 'pk' """
        sio.emit("season", {"msg": "season edited"})
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ Delete an object based on the given ID"""
        sio.emit("season", {"msg": "season deleted"})
        return self.destroy(request, *args, **kwargs)

from django.shortcuts import render
from rest_framework import mixins, generics
from socketio_server import sio
from .models import StyleCombo
from .serializers import StyleComboSerializer

# Create your views here.


class StyleComboListCreateView(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               generics.GenericAPIView):
    queryset = StyleCombo.objects.all()
    serializer_class = StyleComboSerializer

    def get(self, request, *args, **kwargs):
        """Lists the complete list of Style combos"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Creates a new StyleCombo"""
        sio.emit("stylecombo", {"msg": "new stylecombo created"})
        return self.create(request, *args, **kwargs)


class StyleComboDetailUpdateDeleteView(mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       generics.GenericAPIView):
    queryset = StyleCombo.objects.all()
    serializer_class = StyleComboSerializer

    def get(self, request, *args, **kwargs):
        """Retrieves a single object based on the pk"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates an object based on the given pk"""
        sio.emit("stylecombo", {"msg": "stylecombo updated"})
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Deletes an object based on the pk"""
        sio.emit("stylecombo", {"msg": "stylecombo deleted"})
        return self.destroy(request, *args, **kwargs)

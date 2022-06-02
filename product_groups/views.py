from django.shortcuts import render
from rest_framework import mixins, generics
from socketio_server import sio
from .models import ProductGroup
from .serializers import ProductGroupSerializer

# Create your views here.


class ProductGroupListCreateAPIView(mixins.ListModelMixin,
                                    mixins.CreateModelMixin,
                                    generics.GenericAPIView):

    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer

    def get(self, request, *args, **kwargs):
        """Lists all the product groups"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Creates a new product group."""
        sio.emit('product_group', {
            'msg': 'product group added'})
        return self.create(request, *args, **kwargs)


class ProductGroupDetailUpdateDeleteView(mixins.RetrieveModelMixin,
                                         mixins.UpdateModelMixin,
                                         mixins.DestroyModelMixin,
                                         generics.GenericAPIView):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer

    def get(self, request, *args, **kwargs):
        """Retrieves a single object based on the given pk"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates an object based on the given pk"""
        sio.emit("product_group", {'msg': 'product group updated'})
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Deletes the object based on the given pk"""
        sio.emit("product_group", {'msg': 'product group deleted'})
        return self.destroy(request, *args, **kwargs)

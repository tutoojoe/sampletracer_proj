from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from .models import Style
from .serializers import (StyleCreateSerializer,
                          StyleDetailedSerializer,
                          StyleSerializer,
                          )


from socketio_server import sio


# Create your views here.
from rest_framework import mixins
from rest_framework import generics


class StylesListView(generics.ListAPIView):
    """
    Returns a list of all the styls
    """
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


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


class StyleDetailEditUpdateDeleteView(mixins.RetrieveModelMixin,
                                      mixins.UpdateModelMixin,
                                      mixins.DestroyModelMixin,
                                      generics.GenericAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

    def get(self, request, *args, **kwargs):
        """Retrieves a single Style/Product object"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Edits/Updates a Style/Product object"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Deletes a Style object based on the given PK"""
        return self.destroy(request, *args, **kwargs)


# class StyleDetailEditUpdateDeleteView(APIView):
#     # class StyleDetailEditUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Create a new Style (Product)
#     """
#     # serializer_class = StyleSerializer
#     # queryset = Style.objects.all()

#     def get_object(self, pk):
#         try:
#             return Style.objects.get(pk=pk)
#         except Style.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         style = self.get_object(pk)
#         serializer = StyleSerializer(style)
#         return Response(serializer.data)

#     @sio.event
#     def put(self, request, pk, format=None):
#         style = self.get_object(pk)
#         serializer = StyleSerializer(style, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             sio.emit('style_edited', {'data': 'Style Edited'})
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     @sio.event
#     def delete(self, request, pk, format=None):
#         style = self.get_object(pk)
#         style.delete()
#         sio.emit('style_deleted', {'data': 'Style Deleted'})
#         return Response(status=status.HTTP_204_NO_CONTENT)

from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Comments
from .serializer import CommentSerializer

# Create your views here.


class CommentListCreateView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def get(self, request, *args, **kwargs):
        """Returns a list of all the comments """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Create a new comment"""
        return self.create(request, *args, **kwargs)


class CommentRetrieveUpdateDeleteView(mixins.RetrieveModelMixin,
                                      mixins.UpdateModelMixin,
                                      mixins.DestroyModelMixin,
                                      generics.GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def get(self, request, *args, **kwargs):
        """Retrieve a single comment based on pk"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update a single comment based on pk"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete a single comment based on PK"""
        return self.destroy(request, *args, **kwargs)


class CommentsInAStyleView(generics.ListAPIView):
    """Returns all the comments received for a particular style, based on the 'pk' of the style"""
    serializer_class = CommentSerializer

    def get_queryset(self):
        style = self.kwargs['style']
        return Comments.objects.filter(style=style)

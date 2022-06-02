from django.urls import path
from .views import *

urlpatterns = [
    path('', CommentListCreateView.as_view(), name='comments'),
    path('<int:pk>/', CommentRetrieveUpdateDeleteView.as_view(),
         name='comment_detail'),
    path('style/<int:pk>/', CommentsInAStyleView.as_view(),
         name='comments_in_a_style')
]

from django.urls import path
from accounts.views import GoogleLogin, UserList

urlpatterns = [
    path('api/user/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/userlist/', UserList.as_view(), name='user-list')
]

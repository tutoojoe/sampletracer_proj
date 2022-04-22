from django.urls import path
from useraccounts.views import CustomerList

from useraccounts.views import GoogleLogin, UserList, UpdateUserView, UserDetailView

urlpatterns = [
    path('api/user/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/userlist/', UserList.as_view(), name='user_list'),
    path('api/updateuser/<int:pk>/', UpdateUserView.as_view(), name='user_update'),
    path('api/user_details/<int:pk>/',
         UserDetailView.as_view(), name='user_detail'),
    path('api/customers/', CustomerList.as_view(), name='customer_list'),


    # path('api/add_user')
]

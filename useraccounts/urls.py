from django.urls import path
from useraccounts.views import DashboardAPIView, GoogleLogin, UsersListAPIView, UserTypeDetailAPIView, CustomerListAPIView, CustomerDetailAPIView, MerchandiserListAPIView, MerchandiserDetailAPIView

urlpatterns = [
    # google auth
    #     path('api/user/google/', GoogleLogin.as_view(), name='google_login'),

    # dashboard
    path('api/dashboard/', DashboardAPIView.as_view(), name='dashboard'),


    # users
    path('api/users/', UsersListAPIView.as_view(), name='user_list'),
    path('api/users/<int:pk>/',
         UserTypeDetailAPIView.as_view(), name='user_type_detail'),

    # customers
    path('api/customers/', CustomerListAPIView.as_view(),
         name='customer_list'),
    path('api/customers/<int:pk>/',
         CustomerDetailAPIView.as_view(), name='customer_detail'),

    # merchandisers
    path('api/merchandisers/', MerchandiserListAPIView.as_view(),
         name='merchandiser_list'),
    path('api/merchandisers/<int:pk>/',
         MerchandiserDetailAPIView.as_view(), name='merchandiser_detail'),

    # path('api/add_user')
]

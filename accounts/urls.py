from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginUser.as_view(), name='login-user'),
    path('register/', RegisterUser.as_view(), name='register-user'),
    path('logout/', LogoutUser.as_view(), name='logout-user'),
]

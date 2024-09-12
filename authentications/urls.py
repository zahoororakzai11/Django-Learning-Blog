from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from authentications.views import *

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register-user"),
    path("login/", LoginView.as_view(), name="LoginView"),
    path("verity-otp/", VerifyOTPView.as_view(), name="verify-otp"),
    path('author/',AuthorView.as_view(),name='Author-post-get-api'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='autor-detail-api'),
    path('posts/',PostView.as_view(),name="Post-get-post-api"),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]

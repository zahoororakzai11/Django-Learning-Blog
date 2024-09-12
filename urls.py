from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", authtoken_views.obtain_auth_token),
    path("", include("app.urls")),
    path("api/auth/", include("authentications.urls")),
]

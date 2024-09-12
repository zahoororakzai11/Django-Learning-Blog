from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"UserProfile", UserProfileViewSet)
# router.register(r"comment", CommentViewset)
router.register(r"items", ItemViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"resources", ResourceViewSet)

urlpatterns = [
    path("api/app/", include(router.urls)),
]

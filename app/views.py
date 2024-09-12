from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourcesSerializers
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

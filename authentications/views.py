from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from authentications.serializers import *
from authentications.models import *


class CreateUserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    # permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(
                {"success": True, "message": "Registration Successful!"},
                status=200,
            )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    """Login with email and password"""

    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "success": True,
                "user": user.id,
                "message": "Login Successful. Proceed to 2FA",
            },
            status=200,
        )


class VerifyOTPView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer
    # permission_classes = [IsAdminUser]

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login_info: dict = serializer.save()
        return Response(login_info, status=200)

class AuthorView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    # permission_classes = [IsAdminUser]
    queryset = Author.objects.all()


class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    # def post(self,request):
    #     serializers = self.get_serializer(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response({"message":"Successfully Create"},status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
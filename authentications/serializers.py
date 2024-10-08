from datetime import datetime, timezone
from io import BytesIO
import pyotp
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from authentications.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs: dict):
        email = attrs.get("email").lower().strip()
        if get_user_model().objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError({"phone": "Email already exists!"})
        return super().validate(attrs)

    def create(self, validated_data: dict):
        otp_base32 = pyotp.random_base32()
        email = validated_data.get("email")
        otp_auth_url = pyotp.totp.TOTP(otp_base32).provisioning_uri(
            name=email.lower(), issuer_name="Ridwan Ray"
        )
        user_info = {
            "email": validated_data.get("email"),
            "password": make_password(validated_data.get("password")),
            "otp_base32": otp_base32,
        }
        user: User = get_user_model().objects.create(**user_info)
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["id", "email", "password"]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, attrs: dict):
        email = attrs.get("email").lower().strip()
        user = authenticate(
            request=self.context.get("request"),
            email=email,
            password=attrs.get("password"),
        )
        if user is None:
            raise exceptions.AuthenticationFailed("Invalid login details.")
        else:
            attrs["user_object"] = user
        return super().validate(attrs)

    def create(self, validated_data: dict):
        user = User = validated_data.get("user_object")
        totp = pyotp.TOTP(user.otp_base32).now()
        user.login_otp = make_password(totp)
        user.otp_created_at = datetime.now(timezone.utc)
        user.login_otp_used = False
        user.save(update_fields=["login_otp", "otp_created_at", "login_otp_used"])
        return user


class VerifyOTPSerializer(serializers.Serializer):
    otp = serializers.CharField()
    user_id = serializers.UUIDField()

    def validate(self, attrs: dict):
        user: User = User.objects.filter(id=attrs.get("user_id")).first()
        if not user:
            raise exceptions.AuthenticationFailed("Authentication Failed.")
        # if user.login_otp != attrs.get("otp") or not user.is_valid_otp():
        if (
            not check_password(attrs.get("otp"), user.login_otp)
            or not user.is_valid_otp()
        ):
            raise exceptions.AuthenticationFailed("Authentication Failed.")
        attrs["user"] = user
        return super().validate(attrs)

    def create(self, validated_data: dict):
        user: User = validated_data.get("user")
        refresh = RefreshToken.for_user(user)
        user.login_otp_used = True
        user.save(update_fields=["login_otp_used"])
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__" 
    
    def create(self, validated_data):
        authors = validated_data.pop('author',[])
        post = Post.objects.create(**validated_data)
        post.author.set(authors)
        return post

    def update(self, instance, validated_data):
        authors = validated_data.pop('author',None)
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.published_date = validated_data.get('published_date',instance.published_date)
        instance.save()
        if authors is not None:
            instance.author.set(authors)
        return instance
        

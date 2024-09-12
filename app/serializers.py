from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import *


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    bio = serializers.CharField(source="userprofile.bio")
    birth_date = serializers.DateField(source="userprofile.birth_date")

    class Meta:
        model = User
        fields = "__all__"

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "description", "price", "created_at", "updated_at"]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

        # Custome Fields Validation
        def validate_rating(self, value):
            if value < 1 or value > 10:
                raise serializers.ValidationError("Rating has to be betweeen 1 and 10")
            return value

        # Object Level Validations
        def validate(self, data):
            if data["us_gross"] > data["worldwide_gross"]:
                raise serializers.ValidationError(
                    "Us Gros can't be greater than Worldwide grow"
                )
            return data


# Resources Serializers
class ResourcesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"

    # Custom Representation

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['key'] = self.context['key']               : passing through context
        representation["likes"] = instance.liked_by.count()
        return representation

    def to_internal_value(self, data):
        resource_data = data["resource"]
        return super().to_internal_value(resource_data)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = "__all__"
        depth = 1  # Nested Serializers using depth

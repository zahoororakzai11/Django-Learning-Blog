from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk',
            read_only=True
    )
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    this_is_not_real = serializers.CharField(read_only = True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'this_is_not_real',
            'id'
        ]
    def get_my_user_data(self,obj):
        return {
            'username':obj.user.username
        }

    def get_other_products(self,obj):
        user = obj
        my_products_qs = user.product_set.all()[:5]
        return UserPublicSerializer(my_products_qs,many=True,context= self.context).data
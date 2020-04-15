from rest_framework import serializers
from .models import Product
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "owner", "name", "category", "price", "image1", 'quantity']

    def get_category(self, obj):
        return "%s" % (obj.category.name)

    def get_owner(self, obj):
        return "%s" % (obj.owner.username)


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = '__all__'

    def get_category(self, obj):
        return "%s" % (obj.category.name)

    def get_owner(self, obj):
        return "%s" % (obj.owner.username)

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category','price','image1','quantity']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(username=my_username)
        except:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError(
                "Incorrect username or password!")
        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)

        data["access"] = token
        return data

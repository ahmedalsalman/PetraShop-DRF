from rest_framework import serializers
from .models import Product, Cart
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

class CartSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    product = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields='__all__'
    def get_user(self, obj):
        return "%s" % (obj.user.username)
class CartUpdateSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields='product'
#------------------------------------------------------------------------------------------------
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username', 'password']

    def create(self, validated_data):
        first_name=validated_data['first_name']
        last_name=validated_data['last_name']
        email=validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.first_name=(first_name)
        new_user.last_name=(last_name)
        new_user.email=(email)
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

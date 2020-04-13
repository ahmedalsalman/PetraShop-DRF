from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "owner", "name", "category", "price", "image1"]

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

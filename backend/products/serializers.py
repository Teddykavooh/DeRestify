from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serializer
    """
    # field not to be get_dicount as in models
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
        ]

    def get_discount(self, obj):
        """
        Get discount property from models
        """
        # print("NUGU ici: ")
        # print(obj.get_discount)
        return obj.get_discount

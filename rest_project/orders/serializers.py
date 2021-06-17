from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_sum(self,obj):
        total_sum = obj.product.price * obj.quantity
        obj.total_sum = total_sum
        obj.save()
        return total_sum

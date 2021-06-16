from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.Serializer):
    text = serializers.CharField()

class  ProductDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id','photo','name','desc','price','category','comment_set','avg_score']


class RateSerializer(serializers.Serializer):
    score = serializers.FloatField(min_value=1.0, max_value=5.0)
from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product
from .models import Comment
from .serializers import *
from .services import *


class ProductDetailView(APIView):

    def get(self,request,*args,**kwargs):
        product = Product.objects.get(id=kwargs['product_id'])
        rates = product.rate_set.all()
        count_avg_score(rates,product)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        profile = request.user.profile
        product = Product.objects.get(id=kwargs['product_id'])
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.data.get('text')
            if comment_validate(text):
                Comment.objects.create(profile=profile,product=product,text=text)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            raise ValidationError('bad boy')
        return Response(serializer.errors)

class RateView(APIView):

    def post(self,request,*args,**kwargs):
        profile = request.user.profile
        product = Product.objects.get(id=kwargs['product_id'])
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            score = serializer.data.get('score')
            Rate.objects.create(score=score,profile=profile,product=product)

            return Response('score created!',status=201)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

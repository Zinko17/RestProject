from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

class OrderPostView(APIView):

    def post(self,request,*args,**kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,201)
        return Response(serializer.errors,400)
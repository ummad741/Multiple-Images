from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema,swagger_serializer_method
from rest_framework.parsers import MultiPartParser,FormParser
from tasksapp.models import HouseImage, House
from rest_framework import viewsets
from tasksapp.serializers import MainSerializer
# Create your views here.


class CreatePhotoView(APIView):
    serializer = MainSerializer
    # parser_classes = (MultiPartParser,)

    @swagger_auto_schema(request_body=MainSerializer)
    def post(self, request):
        serializer=self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Created",status=status.HTTP_201_CREATED)

        return Response("Error", status=status.HTTP_400_BAD_REQUEST)

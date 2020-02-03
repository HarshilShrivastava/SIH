from django.shortcuts import render
from .models import Company,Jobs
from rest_framework import status
from rest_framework.response import Response 
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .serializers import companyserializer,jobserializer
from rest_framework.views import APIView


class Companyprofile(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if request.user.Is_Organization == 1:
            serializer = companyserializer(data=request.data)
            if serializer.is_valid():
                serializer.save(User=self.request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response( status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if request.user.Is_Organization == 1:
            obj=get_object_or_404(Company,User=request.user)
            serializer = companyserializer(obj)
            return Response(serializer.data)
    def put(self, request, *args, **kwargs):
        if request.user.Is_Candidate == 1:
            obj=get_object_or_404(Company,User=request.user)
            serializer = companyserializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Jobsprofile(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if request.user.Is_Organization == 1:
            serializer=jobserializer(data=request.data)
            if serializer.is_valid():
                a=request.user
                obj=Company.objects.get(User=request.user)
                serializer.save(From=obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response( status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs):
        obj=Company.objects.get(User=request.user)
        qs=Jobs.objects.filter(by=obj)
        serializer=jobserializer(qs,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def detail(request,id):
    qs=Jobs.objects.filter(id=id)
    serializer=jobserializer(qs,many=True)
    return Response(serializer.data)






        
    


        

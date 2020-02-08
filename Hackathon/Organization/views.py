from django.shortcuts import render
from .models import Company,Jobs
from rest_framework import generics

from rest_framework import status
from rest_framework.response import Response 
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .serializers import companyserializer,jobserializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


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


class jobviewset(viewsets.ModelViewSet):
    serializer_class = jobserializer
    queryset=Jobs.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    http_method_names=['get','post','put','delete']
    def create(self, request,*kwargs):
        context={}
        data={}
        user=self.request.user
        companyobj=Company.objects.get(User=self.request.user)
        serializer=jobserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(by=companyobj)
            context['sucess']=True
            context['response']="sucessfull"
            context['status']=200
            data=serializer.data
            context['data']=data
            return Response(context)
        else:
            return Response(serializer.errors)


    def list(self, request,*kwargs):
        context={}
        data={}
        user=self.request.user
        companyobj=get_object_or_404(Company,User=user)
        queryset=Jobs.objects.filter(by=companyobj)
        context['sucess']=True
        context['status']=200
        context['response']="sucessfull"
        serializer = jobserializer(queryset,many=True)
        data=serializer.data
        context['data']=data
        return Response(context)
    def post(self,request,*kwargs):
        context={}
        data={}
        user=self.request.user
        companyobj=get_object_or_404(Company,User=self.request.user)
        serializer=jobserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(by=companyobj)
            context['sucess']=True
            context['response']="sucessfull"
            context['status']=200
            data=serializer.data
            context['data']=data
            return Response(context)



class RecommendedJobviewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = jobserializer
    queryset=Jobs.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Level','fields']

    http_method_names=['get']
    def list(self, request,*kwargs):
        context={}
        data={}
        queryset=Jobs.objects.all()
        context['sucess']=True
        context['status']=200
        context['response']="sucessfull"
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        data=serializer.data
        context['data']=data
        return Response(context)


        

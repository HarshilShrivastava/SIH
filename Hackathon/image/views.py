from django.shortcuts import render

# Create your views here.fr
from .models import image
from .serializers import AnswerSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class QuestiontListViewset(viewsets.ModelViewSet):
    queryset = image.objects.all()
    serializer_class = AnswerSerializer
    #3http_method_names = ['get','POST']


    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'Question_list': serializer.data})
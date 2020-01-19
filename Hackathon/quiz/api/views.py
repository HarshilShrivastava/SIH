from quiz.models import(
     Answer,
     DomainQuestion,
     Question
)
from quiz.api.serializers import (
QuestionSerializer,
AnswerSerializer,
DomainQuestionSerializer,
DomainMarksSerializer,
GeneralMarksSerializer

)
from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.response import Response

class QuestiontListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ['get']
    #filter_backends = [DjangoFilterBackend]
    #filter_fields = ['JEWELLER_ID', 'ORNAMENT_TYPE','ORNAMENT_MATERIAL','ORNAMENT_SHOPFOR']    

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'Question_list': serializer.data})

class DomainQuestiontListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = DomainQuestion.objects.all()
    serializer_class = DomainQuestionSerializer
    http_method_names = ['get']
    #filter_backends = [DjangoFilterBackend]
    #filter_fields = ['JEWELLER_ID', 'ORNAMENT_TYPE','ORNAMENT_MATERIAL','ORNAMENT_SHOPFOR']    

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'Question_list': serializer.data})


@api_view( ['POST'])

def putgeneralmarks(request):
    if request.method=="POST":
        serializer=GeneralMarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view( ['POST'])

def putdomainmarks(request):
    if request.method=="POST":
        serializer=DomainMarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



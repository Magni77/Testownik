from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    )
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from tests.models import TestModel, QuestionModel, AnswerModel
from .serializers import TestSerializer, TestListSerializer, QuestionSerializer, AnswerSerializer, UploadFileSerializer
from rest_framework.response import Response
from .models import UploadFileModel
from tests.upload_handler import UploadHandler


class TestListAPIView(ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestListSerializer


class QuestionListAPIView(ListAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


#details
class TestDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer


#create views
class TestCreateAPIView(CreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    #authentication_classes = TokenAuthentication


class QuestionCreateAPIView(CreateAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreateAPIView(CreateAPIView):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer


class TestUploadView(CreateAPIView):
    queryset = UploadFileModel
    serializer_class = UploadFileSerializer

    def create(self, request, filename='22', format=None):
        files = request.FILES.getlist('file')

        UploadHandler(request, files, request, is_rest=True)
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)
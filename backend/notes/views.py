from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import NoteTopic, Note
from .serializers import NoteTopicSerializer, NoteSerializer

class NoteTopicList(generics.ListAPIView):
    serializer_class = NoteTopicSerializer

    def get_queryset(self):
        return NoteTopic.objects.filter(author=self.request.user)


class NoteTopicCreate(generics.CreateAPIView):
    queryset = NoteTopic.objects.all()
    serializer_class = NoteTopicSerializer


class NoteTopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoteTopic.objects.all()
    serializer_class = NoteTopicSerializer


    


class NoteList(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class NoteCreate(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = NoteTopic.objects.all()

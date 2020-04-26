from rest_framework import generics

from .models import NoteTopic, Note
from .serializers import NoteTopicSerializer, NoteSerializer


class NoteTopicList(generics.ListAPIView):
    serializer_class = NoteTopicSerializer
    # queryset = NoteTopic.objects.all()
    def get_queryset(self):
        return NoteTopic.objects.filter(author=self.request.user)


class NoteTopicCreate(generics.CreateAPIView):
    queryset = NoteTopic.objects.all()
    serializer_class = NoteTopicSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = NoteTopic.objects.all()

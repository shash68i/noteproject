from rest_framework import generics

from .models import Timeline
from .serializers import TimelineSerializer


class TimelineList(generics.ListAPIView):
    serializer_class = TimelineSerializer

    def get_queryset(self):
        return Timeline.objects.filter(author=self.request.user)


class TimelineCreate(generics.CreateAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TimelineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
from rest_framework import generics

from .models import Remember
from .serializers import RememberSerializer


class RememberList(generics.ListAPIView):
    serializer_class = RememberSerializer

    def get_queryset(self):
        return Remember.objects.filter(author=self.request.user)


class RememberCreate(generics.CreateAPIView):
    queryset = Remember.objects.all()
    serializer_class = RememberSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RememberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Remember.objects.all()
    serializer_class = RememberSerializer
from rest_framework import serializers
from .models import NoteTopic, Note


class NoteTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteTopic
        fields = ('id', 'topic','created',)

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'notetopic', 'title', 'takeway', 'tech_detail', 'created',)
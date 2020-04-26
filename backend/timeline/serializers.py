from rest_framework import serializers
from .models import Timeline


class TimelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeline
        fields = ('id', 'title', 'content', 
            'goal_term', 'status', 'created', 'updated',)
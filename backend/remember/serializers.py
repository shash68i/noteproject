from rest_framework import serializers
from .models import Remember


class RememberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Remember
        fields = ('id', 'duration', 'topic','resources', 'created',)
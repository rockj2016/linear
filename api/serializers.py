from rest_framework import serializers

from .models import Event, EventLog


class EventSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Event
        fields = '__all__'


class EventLogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    event = serializers.ReadOnlyField(source='event.name')

    class Meta:
        model = EventLog
        fields = '__all__'

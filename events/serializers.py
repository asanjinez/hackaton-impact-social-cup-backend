from django.contrib.auth import get_user_model
from .models import Event, Participant, Task, Reminder
from rest_framework import serializers, permissions

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["organizer", "title", "description", "event_date", "location"]
        read_only_fields = ["organizer"]
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ["user", "event", "collaborator", "status"]
        read_only_fields = ["user"]
        permission_classes = [permissions.IsAuthenticated]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["event", "name", "description", "assignee", "completed"]
        permission_classes = [permissions.IsAuthenticated]


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ["task", "assignee", "date"]
        permission_classes = [permissions.IsAuthenticated]

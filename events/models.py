from django.conf import settings
from django.db import models
from django.utils import timezone


class Event(models.Model):
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organized_events",
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="joined_events", blank=True
    )

    STATUS_CHOICES = [
        ("upcoming", "Próximo"),
        ("ongoing", "En Curso"),
        ("completed", "Finalizado"),
        ("cancelled", "Cancelado"),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="upcoming")

    def __str__(self):
        return self.title


class Task(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    assignee = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Reminder(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="reminders",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()

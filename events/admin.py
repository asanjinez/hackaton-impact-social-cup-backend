from django.contrib import admin
from .models import Event, Task, Reminder, Participant


class ParticipantInLine(admin.StackedInline):
    model = Participant
    extra = 0


class TaskInline(admin.StackedInline):
    model = Task
    extra = 0

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        formfield = super().formfield_for_manytomany(db_field, request, **kwargs)

        if db_field.name == "assignee":
            event_id = request.resolver_match.kwargs.get("object_id")
            if event_id:
                formfield.queryset = Participant.objects.filter(event_id=event_id)
        return formfield


class EventAdmin(admin.ModelAdmin):
    inlines = [ParticipantInLine, TaskInline]


admin.site.register(Event, EventAdmin)


class ReminderInline(admin.StackedInline):
    model = Reminder
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == "assignee":
            task_id = request.resolver_match.kwargs.get("object_id")
            if task_id:
                print("======================")
                formfield.queryset = Task.objects.get(id=task_id).assignee.all()
        return formfield


class TaskAdmin(admin.ModelAdmin):
    inlines = [ReminderInline]


admin.site.register(Task, TaskAdmin)

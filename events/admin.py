from django.contrib import admin
from .models import Event, Task, Reminder

admin.site.register(Event)


class RemainderInline(admin.StackedInline):
    model = Reminder
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    inlines = [RemainderInline]


admin.site.register(Task, TaskAdmin)

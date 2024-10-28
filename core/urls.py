from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from events import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"events", views.EventViewSet)
router.register(r"participants", views.ParticipantViewSet)
router.register(r"tasks", views.TaskViewSet)
router.register(r"reminders", views.ReminderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]

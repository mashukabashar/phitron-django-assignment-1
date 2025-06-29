from django.urls import path
from events.views import dashboard, create_event, update_event, delete_event

urlpatterns = [
    path("dashboard/",dashboard, name='dashboard'),
    path("create-event/",create_event, name="create-event"),
    path("update-event/<int:id>/",update_event, name="update-event"),
    path("delete-event/<int:id>/",delete_event, name="delete-event"),
]

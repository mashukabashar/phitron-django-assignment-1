from django.urls import path
from events.views import dashboard, create_event, update_event, delete_event, create_category, update_category, create_participant, update_participant

urlpatterns = [
    path("dashboard/",dashboard, name='dashboard'),

    path("create-event/",create_event, name="create-event"),
    path("update-event/<int:id>/",update_event, name="update-event"),
    path("delete-event/<int:id>/",delete_event, name="delete-event"),

    path("create-category/",create_category, name="create-category"),
    path("update-category/<int:id>/",update_category, name="update-category"),

    path("create-participant/",create_participant, name="create-participant"),
    path("update-participant/<int:id>/",update_participant, name="update-participant"),
]

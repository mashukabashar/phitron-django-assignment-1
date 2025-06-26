from django.urls import path
from events.views import show_event, contact, show_specific_event

urlpatterns = [
    path('show_event/',show_event),
    path('contact/',contact),
    path("show_event/<int:id>/",show_specific_event),
    # path("show_event/<id>/",show_specific_event)
]

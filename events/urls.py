from django.urls import path
from events.views import show_event, contact

urlpatterns = [
    path('show_event/',show_event),
    path('contact/',contact),
]

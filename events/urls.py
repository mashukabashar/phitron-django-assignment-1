from django.urls import path
from events.views import dashboard, test, create_event, view_event

urlpatterns = [
    # path('show_event/',show_event),
    # path('contact/',contact),
    # path("show_event/<int:id>/",show_specific_event),
    # path("show_event/<id>/",show_specific_event),
    path("dashboard/",dashboard),
    path("test/",test),
    path("create-event/",create_event),
    path("view-event/",view_event)
]

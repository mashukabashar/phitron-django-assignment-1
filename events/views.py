from django.shortcuts import render, redirect
from django.http import HttpResponse
from events.forms import EventModelForm
from events.models import Category, Event, Participant
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg
from django.contrib import messages


# Create your views here.

# def show_event(request):
#     return HttpResponse("<h1 style='color:green'>This is our event list</h1>")

# def contact(request):
#     return HttpResponse("<h1>This is our contact page</h1>")

# def show_specific_event(request, id):
#     print("id", id)
#     print("id type", type(id))
#     return HttpResponse(f"This is specific event page {id}");


def home(request):
    return HttpResponse("<h1 style='color:red'>Welcome To The Event Management System</h1>")




def dashboard(request):

    events=Event.objects.select_related("category").prefetch_related("guests").all()

    counts = Event.objects.aggregate(
        total=Count('id'),
        past_events=Count('id', filter=Q(date__lt=date.today())),
        future_events=Count('id', filter=Q(date__gt=date.today())),
        today_event=Count('id', filter=Q(date=date.today())),
    )

    context={"events":events, "counts":counts}

    return render(request, "dashboard.html", context)





def test(request):
    names= ["Mashuka","Diya", "Ananna", "Priyongboda"]
    count=0
    for name in names:
        count=count+1

    context={"names": names,
             "age":23,
             "count":count}
    
    return render(request, "test.html", context)




def create_event(request):
    participants=Participant.objects.all()
    form = EventModelForm()  # For GET

    if request.method == "POST":
        form = EventModelForm(request.POST)

        if form.is_valid():

            form.save()
            return render(request, "event_form.html", {"form": form, "message": "Event Added Successfully"})
        
    context={"form":form}
    return render(request, "event_form.html", context)



def view_event(request):


    # events=Event.objects.all()
    # event1=Event.objects.get(id=1)
    # return render(request, "show_event.html",{"categories":categories, "event_1":event1})


    categories=Category.objects.prefetch_related('event').all()
    return render(request, "show_event.html",{"categories":categories})



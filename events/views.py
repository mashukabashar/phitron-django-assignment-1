from django.shortcuts import render, redirect
from django.http import HttpResponse
from events.forms import EventModelForm, CategoryModelForm, ParticipantModelForm
from events.models import Category, Event, Participant
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg
from django.contrib import messages
from django.utils.timezone import localdate


def home(request):
    return render(request, "home.html")




def dashboard(request):
    type=request.GET.get('type','all')

    events=Event.objects.select_related("category").prefetch_related("guests").all()
    participants=Participant.objects.all()

    counts = Event.objects.aggregate(
        total=Count('id'),
        past_events=Count('id', filter=Q(date__lt=date.today())),
        future_events=Count('id', filter=Q(date__gt=date.today())),
        today_event=Count('id', filter=Q(date=date.today())),
    )

    unique_participant_count = Participant.objects.filter(events__isnull=False).distinct().aggregate(total=Count('id'))

    base_query=Event.objects.select_related("category").prefetch_related("guests")

    if type=='all':
        events=base_query.all()

    elif type=='past_events':
        events=base_query.filter(Q(date__lt=date.today()))

    elif type=='future_events':
        events=base_query.filter(Q(date__gt=date.today()))

    elif type=='today_event':
        events=base_query.filter(Q(date=date.today()))

    elif type=="total_participants":
        participants=Participant.objects.filter(events__isnull=False).distinct()



    context={"events":events, 'participants':participants, "counts":counts, "unique_participant_count":unique_participant_count, "type":type}

    return render(request, "dashboard.html", context)




def create_event(request):
    participants=Participant.objects.all()
    form = EventModelForm()  # For GET

    if request.method == "POST":
        form = EventModelForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request,'Event Created Successfully')
            return redirect('create-event')
        
    context={"form":form}
    return render(request, "event_form.html", context)


def create_category(request):
    category=Category.objects.all()
    form = CategoryModelForm()  # For GET

    if request.method == "POST":
        form = CategoryModelForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request,'Category Created Successfully')
            return redirect('create-category')
        
    context={"form":form}
    return render(request, "category_form.html", context)


def create_participant(request):
    participant=Participant.objects.all()
    form = ParticipantModelForm()  # For GET

    if request.method == "POST":
        form = ParticipantModelForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request,'Participant Created Successfully')
            return redirect('create-participant')
        
    context={"form":form}
    return render(request, "participant_form.html", context)




def update_event(request, id):
    event=Event.objects.get(id=id)

    participants=Participant.objects.all()
    form = EventModelForm(instance=event)  # For GET & instance for update 

    if request.method == "POST":
        form = EventModelForm(request.POST, instance=event) # instance for update

        if form.is_valid():

            form.save()
            messages.success(request,'Event Updated Successfully')
            return redirect('update-event', id)
        
    context={"form":form}
    return render(request, "event_form.html", context)


def update_category(request, id):
    category=Category.objects.get(id=id)

    participants=Participant.objects.all()
    form = CategoryModelForm(instance=category)  # For GET & instance for update 

    if request.method == "POST":
        form = CategoryModelForm(request.POST, instance=category) # instance for update

        if form.is_valid():

            form.save()
            messages.success(request,'Category Updated Successfully')
            return redirect('update-category', id)
        
    context={"form":form}
    return render(request, "category_form.html", context)

# dashboard e edit button create kore okhan theke update category page e jabe



def update_participant(request, id):
    participant=Participant.objects.get(id=id)

    participants=Participant.objects.all()
    form = ParticipantModelForm(instance=participant)  # For GET & instance for update 

    if request.method == "POST":
        form = ParticipantModelForm(request.POST, instance=participant) # instance for update

        if form.is_valid():

            form.save()
            messages.success(request,'Participant Updated Successfully')
            return redirect('update-participant', id)
        
    context={"form":form}
    return render(request, "participant_form.html", context)

# dashboard e edit button create kore okhan theke update participant page e jabe


def delete_event(request, id):

    if request.method == "POST":
        event=Event.objects.get(id=id)
        event.delete()

        messages.success(request,'Event Deleted Successfully')
        return redirect('dashboard')
    else:
        messages.error(request,'Something Went Wrong!')
        return redirect('dashboard')







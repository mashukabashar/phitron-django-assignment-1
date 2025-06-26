from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, "dashboard.html")

def test(request):
    names= ["Mashuka","Diya", "Ananna", "Priyongboda"]
    count=0
    for name in names:
        count=count+1

    context={"names": names,
             "age":23,
             "count":count}
    
    return render(request, "test.html", context)

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style='color:red'>Welcome To The Event Management System</h1>")

def show_event(request):
    return HttpResponse("<h1 style='color:green'>This is our event list</h1>")

def contact(request):
    return HttpResponse("<h1>This is our contact page</h1>")
from django.shortcuts import render,redirect
from django.http import HttpResponse
from manage.models import Posts
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import get_object_or_404

def login(request):
    return HttpResponse(render(request,"home.html",{}))
    
def about(request):
    return render(request,"About.html",{})  

def contact(request):
    return render(request,"contact.html",{})
    
def log(request):
    return render(request,"log.html",{}) 

def new(request):
    return render(request,"new.html",{})       

def registered(request):
    return render(request,"registered.html",{})          
# Create your views here.

def bookings(request):
   
    return render(request,"ViewBookings.html",{})    

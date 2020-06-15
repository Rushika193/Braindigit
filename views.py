from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        return render(request, 'index.html',{'content':'click on submit'})

#def home(request):
    
    #return HttpResponse("hello world")

def profile(request):
    return HttpResponse("profile page")




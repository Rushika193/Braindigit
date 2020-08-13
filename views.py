from django.shortcuts import render,redirect
from django.http import HttpResponse
from manage.models import Posts,Status,Paid,Book,Appointment,Usern
from django.contrib.auth.forms import UserCreationForm
from manage.forms import PostForm,bookappointment,appointmentform
from django.contrib.auth import authenticate, login 
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.template import RequestContext
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def logintohome(request):
    return HttpResponse(render(request,"home.html",{}))
    
def about(request):
    return render(request,"About.html",{})  

def contact(request):
    return render(request,"contact.html",{})

    
def new(request):
    
    if request.method=='POST': 
        form=PostForm(request.POST)
        if form.is_valid():
             form.save()
             user=form.cleaned_data.get('username')
             messages.success(request,"Registration is done for " + user)
             return redirect('log/')   
    else:
          form=PostForm()
    return render(request,"new.html",{'form':form})  
    
def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user1=authenticate(request,username=username,password=password)
       
        if user1 is not None:
            login(request, user1)
            return redirect('registered/')
        else:
            messages.info(request,"Username or password is not correct")    
    return render(request,"log.html",{})      

def adminsignup(request):
    form=PostForm(request.POST)
    if request.method=='POST':
        
        if form.is_valid():
            form.save()
            return redirect('Adminlogin/')   
    return HttpResponse(render(request,"adminsignup.html",{'form':form}))

def Adminlogin(request):
    if request.method=='POST':
        u=request.POST.get('username')
        p=request.POST.get('password')
        user=authenticate(username=u,password=p) 
        if user is not None:
            login(request,user)
            return redirect('page/')
        else:
            messages.info(request,"Password or username is not correct")    
    return render(request,"admin.html",{})

def registered(request):
     return HttpResponse(render(request,"registered.html",{}))          
# Create your views here.

def bookings(request):
    book=Book.objects.all()
    user=Usern.objects.all()
    app=Appointment.objects.all()
    error=""
    if request.method=='POST':
        a=request.POST['des']
        t=request.POST['time']
        d=request.POST['date']
        try:
            error="No"
            Book.objects.create(Design=a,time=t,date=d)
        except:
            error="Yes"   
    return render(request,"bookings.html",{'error':error})

def appointments(request):
    book=Book.objects.all()
    sta=Status.objects.all()
    error=""
    if request.method=='POST':
        user=request.POST['txt']
        dd=request.POST['des']
        tt=request.POST['time']
        dat=request.POST['date']
        desi=Book.objects.filter(Design=dd).first()
        s= Status.objects.create(status="Pending")
        try:
            error="No"
            Appointment.objects.create(posts=user,design=desi,time=tt,date=dat,stat=s)
        except:
            error="Yes"   
        

    context= {
      'error':error,'desi':book }     
    return render(request,"appointments.html",context)    

  

def viewrequests(request):
    Tot_appointments=Appointment.objects.filter().order_by('date')  
    return render(request,"viewrequests.html",{'Tot_appointments':Tot_appointments})




def logout(request):
    logout(request)
    return redirect('log/')  

def ViewBookings(request):
    pro=Appointment.objects.get(stat="Pending")
    tot_appointment=Appointment.objects.filter(stat=pro)
    return render(request,"ViewBookings.html",{'app':tot_appointment})



def page(request):
    sign=Appointment.objects.all()
    total_appointment_accepted=0
    total_appointment_pending=0
    total_appointment=Appointment.objects.all().count()
    
    for i in sign:
        if i.stat.status=='Accepted':
            total_appointment_accepted+=1
        if i.stat.status=='Pending':
            total_appointment_pending+=1
     

    context={'total_appointment_accepted':total_appointment_accepted,
            'total_appointment_pending':total_appointment_pending,
            'total_appointment':total_appointment}
    return render(request,"adminpage.html",context)  


def book_assign_status(request,pid):
    book=Appointment.objects.get(id=pid)
    form= appointmentform(instance=book)
    if request.method=="POST":
        form= appointmentform(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('viewrequests/')
    return render(request,"status.html",{'form':form})


def book_selected_item(request,pid):
    book=Appointment.objects.get(id=pid)
    if request.method=="POST":
        st=request.POST['status']
        sta= Status.objects.get(status=st)
        book.stat=sta
        book.save()
    return render(request,"ViewBookings.html",{'book':book})    

def delete(request,pid):
    ap=Appointment.objects.get(id=pid)
    ap.delete()
    return redirect('status/viewrequests/')

def pay(request):
        return HttpResponse(render(request,"pay.html",{}))    

    
def status(request,pk):
    app=Appointment.objects.get(id=pk)
    form = appointmentform(instance=app)
    if request.method=="POST":
         form = appointmentform(request.POST,instance=app)
         if form.is_valid():
             form.save()
             return redirect('/viewrequests')
    return render(request,"status.html",{'form':form})
from django import forms
from manage.models import Posts,Appointment,Book,Paid,Status,Usern
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.db import models



class PostForm(UserCreationForm):
   
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2',)

class Userid(UserCreationForm):
    class Meta:
        model=Usern
        fields=('uname',)                
        uname=forms.ModelChoiceField(queryset=User.objects.all())




class bookappointment(forms.ModelForm):
  
    class Meta:
      
        model=Book
        fields = ('name','Design','pub_date','time','date',)
        name=forms.ModelChoiceField(queryset=Usern.objects.all())

class paiddetail(UserCreationForm):
    class Meta:
             model=Paid
             fields=('paid',) 

class statusdetail(UserCreationForm):
    class Meta:
        model=Status
        fields=('status',)

class appointmentform(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=('posts','design','stat','time','date',)
    stat=forms.ModelChoiceField(queryset=Status.objects.all())    
    
    design=forms.ModelChoiceField(queryset=Book.objects.all())

    def clean_service(self):
        Book = self.cleaned_data.get('Book')

class Post(forms.ModelForm):
    class Meta:
        model=Posts
        fields=('FullName','user','PhoneNumber','Address',)
        user=forms.ModelChoiceField(queryset=Usern.objects.all())


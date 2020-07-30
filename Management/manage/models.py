from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Usern(models.Model):
    uname=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self): 
        return self.uname.username
class Posts(models.Model):
    FullName=models.CharField(max_length=120)
    user=models.ForeignKey(Usern,on_delete=models.CASCADE,null=True)
    PhoneNumber=models.IntegerField(null=True)
    Address=models.TextField(max_length=120)
    pub_date = models.DateTimeField(blank=True, null=True)
  
    def publish(self):
        self.pub_date=timezone.now()
        self.save()
  
    def __unicode__(self): 
        return self.user.uname.username

class Book(models.Model):
      name= models.ForeignKey(Usern,on_delete=models.CASCADE,null=True)
      Design= models.CharField(max_length=520,null=True)  
      pub_date = models.DateTimeField(blank=True, null=True) 
      time=models.TimeField(max_length=520,blank=True, null=True)
      date=models.DateField(max_length=520,blank=True, null=True)   
      def __str__(self): 
          return self.Design 

class Status(models.Model):
    status= models.CharField(max_length=120,default="Pending",null=True)             

    def __str__(self): 
          return self.status

class Paid(models.Model):
    paid= models.CharField(max_length=120,null=True) 

    def __str__(self): 
          return self.paid

class Appointment(models.Model):
    posts=models.CharField(max_length=120,null=True)
    stat= models.ForeignKey(Status,on_delete=models.CASCADE,null=True)  
    design= models.ForeignKey(Book,on_delete=models.CASCADE,null=True)  
    time=models.TimeField(default=timezone.now())
    date=models.DateField(default=timezone.now())   

    def __unicode__(self): 
          return self.posts.uname.username+" "+self.design.Design  


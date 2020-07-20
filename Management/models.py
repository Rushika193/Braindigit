from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class Posts(models.Model):
    FullName=models.CharField(max_length=120)
    Email=models.ForeignKey(User,on_delete=models.CASCADE)
    PhoneNumber=models.IntegerField(null=True)
    Address=models.TextField(max_length=120)
    pub_date = models.DateTimeField(blank=True, null=True)
  
    def publish(self):
        self.pub_date=timezone.now()
        self.save()
    def __str__(self): 
        return self.Email.username
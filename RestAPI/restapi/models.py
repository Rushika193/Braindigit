from django.db import models

class employee(models.Model):
    Empname=models.CharField(max_length=150,null=True)
   
    Profession=models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.Empname


# Create your models here.

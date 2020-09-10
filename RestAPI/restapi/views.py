from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import employee
from .serializer import empserializer

class employeelist(APIView):
    def get(self,request):
        employee1=employee.objects.all()
        serializer=empserializer(employee1,many=True)
        return Response(serializer.data)

    def post(self):
        pass    
# Create your views here.

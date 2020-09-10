from rest_framework import serializers
from restapi.models import employee 

class empserializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields=('Empname','Profession',)

from django import forms
from manage.models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=('FullName','PhoneNumber','Address',)
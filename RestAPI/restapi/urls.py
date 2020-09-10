from django.contrib import admin
from django.urls import path,include
from .import views 

app_name="restapi"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.employeelist.as_view()),
]
from django.contrib import admin
from django.urls import path,include
from .import views
admin.autodiscover()
app_name = "manage"
urlpatterns = [
  
    path('',views. logintohome,name="login"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('new/log/',views.log,name="log"),
    path('new/',views.new,name="new"),
    path('new/log/registered/',views.registered,name="registered"),
    path('book/',views.bookings,name="bookings"),
    path('viewrequests/',views.viewrequests,name="viewrequests"),
   # path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminsignup/',views.adminsignup,name="adminsignup"),
    path('logout/',views.logout,name="logout"),
    path('adminsignup/Adminlogin/',views.Adminlogin,name="Adminlogin"),
    path('adminsignup/Adminlogin/page/',views.page,name="page"),
    path('status/viewrequests/',views.viewrequests,name="viewrequests"),
    path('book_selected_item/',views.book_selected_item,name="book_selected_item"),
    path('assign/',views.book_assign_status,name="book_assign_status"),
    path('appointments/',views.appointments,name="appointments"),
    path('delete(?P<int:pid>)',views.delete,name="delete"),
    path('book_assign_status',views.book_assign_status,name="book_assign_status"),
    path('pay/',views.pay,name="pay"),
    path('status/<str:pk>/',views.status,name="status"),
   # path('confirm/',views.confirm,name="confirm")
]

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

admin.autodiscover()
app_name = "a1"

urlpatterns = [
    path('', views.index, name='index'),
    # url(r"^(?P<pk>\d+)/$", views.IndexView.as_view(), name="indexV"),
    # url(r"^(?P<pk>\d+)/$", views.DetailView.as_view(), name="detail"),
    # url(r"^(?P<pk>\d+)/$", views.ResultsView.as_view(), name="results"),
    # url(r"^(?P<pk>\d+)/$", views.vote, name="vote")
    path('post/<int:pk>/', views.p_d, name='p_d'),
    path('post/new/', views.post_new, name='post_new'),
]

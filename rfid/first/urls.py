from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',views.register,name='register'),
       path('signup',views.register1,name='register1'),
    path('home/',views.home,name='home'),

    path('read/',views.read,name='read'),
    path('read1/',views.read1,name='read1'),
    path('signup/',views.signup,name='signup'),
    path('write/',views.register_w1,name='register_w1'),
    path('write2/',views.register_w2,name='register_w2'),
    path('track/',views.track,name='track'),
    path('track2/',views.track2,name='track2'),

]
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('read/',views.read,name='read'),
    path('read1/',views.read1,name='read1'),
    path('read2/',views.read2,name='read2'),
    path('read3/',views.read3,name='read3'),
    path('read4/',views.read4,name='read4'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('write/',views.write,name='write'),
    path('write2/',views.write2,name='write2'),
    path('track/',views.track,name='track'),
    

]



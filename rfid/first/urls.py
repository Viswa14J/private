from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('read/',views.read,name='read'),
    path('read1/',views.read1,name='read1'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('write/',views.write,name='write'),
    path('write2/',views.write2,name='write2'),
    path('track/',views.track,name='track'),
    

]



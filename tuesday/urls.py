from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('userregister/', views.userregister, name='userregister'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('addnew/', views.addnew, name='addnew'),
    path('addnewdata/', views.addnewdata, name='addnewdata'),
    path('logout/', views.logout, name='logout'),

    path('deletedata/<int:eid>', views.deletedata, name='deletedata'),
    path('edituser/<int:eid>', views.edituser, name='edituser'),
    path('updatedata/<int:eid>', views.updatedata, name='updatedata'),

    path('investdata/<int:eid>', views.investdata, name='investdata'),




]

from django.contrib import admin
from django.urls import path
from Diagnostic_Center import views
from Diagnostic_Center.views import *

app_name = 'Diagnostic_Center'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('view_prescription/', views.view_prescription, name='view_prescription'),
    path('view_appointment_doctor/', views.view_appointment_doctor, name='view_appointment_doctor'),
    path('view_appointment_test/', views.view_appointment_test, name='view_appointment_test'),
    path('view_appointment_package_test/', views.view_appointment_package_test, name='view_appointment_package_test'),
    path('create_appointment_doctor/', views.create_appointment_doctor, name='create_appointment_doctor'),
    path('create_appointment_test/', views.create_appointment_test, name='create_appointment_test'),
    path('create_appointment_package_test/', views.create_appointment_package_test, name='create_appointment_package_test'),
    path('create_prescription/', views.create_prescription, name='create_prescription'),
    path('delete_appointment_doctor(<int:pid>)', views.delete_appointment_doctor, name='delete_appointment_doctor'),
    path('delete_appointment_test(<int:pid>)', views.delete_appointment_test, name='delete_appointment_test'),
    path('delete_appointment_package_test(<int:pid>)', views.delete_appointment_package_test, name='delete_appointment_package_test'),
    path('delete_prescription(<int:pid>)', views.delete_prescription, name='delete_prescription'),
    path('view_test/', views.view_test, name='view_test'),
    path('view_package/', views.view_package, name='view_package'),
    
]

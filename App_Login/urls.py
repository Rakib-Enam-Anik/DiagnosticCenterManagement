from django.urls import path
from App_Login import views
from .views import sign_up, DcmAdminSignUpview, DoctorSignUpview, TechnicianSignUpview, CreatePatient
app_name = 'App_Login'

urlpatterns = [
    path('signup/', sign_up,  name='signup'),
    path('dcmadminsignup/', DcmAdminSignUpview.as_view(),  name='dcmadminsignup'),
    path('doctorsignup/', DoctorSignUpview.as_view(),  name='doctorsignup'),
    path('view_doctor/', views.View_Doctor, name='view_doctor'),
    path('delete_doctor(<int:pid>)', views.delete_doctor, name='delete_doctor'),
    path('techniciansignup/', TechnicianSignUpview.as_view(),  name='techniciansignup'),
    path('view_technician/', views.View_Technician, name='view_technician'),
    path('delete_technician(<int:pid>)', views.Delete_Technician, name='delete_technician'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('doctor_profile/', views.doctor_profile, name='doctor_profile'),
    path('technician_profile/', views.technician_profile, name='technician_profile'),
    path('change-profile/', views.user_change, name='user_change'),
    path('change-doctor-profile/', views.doctor_change, name='doctor_change'),
    path('change-technician-profile/', views.technician_change, name='technician_change'),
    path('password/', views.pass_change, name='pass_change'),
    path('add-picture/', views.add_pro_pic, name='add_pro_pic'),
    path('change-picture/', views.change_pro_pic, name='change_pro_pic'),
    path('view_patient/', views.View_Patient, name='view_patient'),
    path('add_patient/', views.CreatePatient, name='add_patient'),
    path('delete_patient(<int:pid>)', views.Delete_Patient, name='delete_patient'),
]

    
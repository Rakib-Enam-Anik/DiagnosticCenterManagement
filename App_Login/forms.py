from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from App_Login.models import User, DcmAdmin, Doctor, Technician


class UserSignUpForm(UserCreationForm):

    email = forms.EmailField( label="Email Address", required=True)
    
    class Meta:
        model = User
        fields = ('username',  'first_name', 'last_name', 'email', 'password1', 'password2')

class AttendentSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',  'first_name', 'last_name', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_dcmadmin = True
        user.save()
        patient = DcmAdmin.objects.create(user=user)
        return user

class DcmAdminSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',  'first_name', 'last_name', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_dcmadmin = True
        user.save()
        patient = DcmAdmin.objects.create(user=user)
        return user
    
class DoctorSignUpForm(UserCreationForm):
    
    
    email=forms.EmailField(required=True)
    doctor_full_name = forms.CharField(required=True)
    phone=forms.IntegerField(required=True)
    spe = forms.CharField(required=True)
    designation=forms.CharField(required=True)
    degree = forms.CharField(required=True)
    current_working_place = forms.CharField(required=True)
    mbbs_institution = forms.CharField(required=True)
    post_graduation_institution = forms.CharField(required=True)
    
  
    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.doctor_full_name = self.cleaned_data.get('doctor_full_name')
        doctor.phone=self.cleaned_data.get('phone')
        doctor.spe=self.cleaned_data.get('spe')
        doctor.designation=self.cleaned_data.get('designation')
        doctor.degree=self.cleaned_data.get('degree')
        doctor.current_working_place=self.cleaned_data.get('current_working_place')
        doctor.mbbs_institution=self.cleaned_data.get('mbbs_institution')
        doctor.post_graduation_institution=self.cleaned_data.get('post_graduation_institution')
        doctor.save()

        return doctor
    

class TechnicianSignUpForm(UserCreationForm):
    email = forms.EmailField( label="Email Address", required=True)
    technician_full_name = forms.CharField(required=True)
    phone=forms.IntegerField(required=True)
    designation=forms.CharField(required=True)
    
  
    class Meta(UserCreationForm.Meta):
        model = User
        
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_technician = True
        user.save()
        technician = Technician.objects.create(user=user)
        technician.technician_full_name = self.cleaned_data.get('technician_full_name')
        technician.phone=self.cleaned_data.get('phone')
        technician.designation=self.cleaned_data.get('designation')
        technician.save()
        return technician
    
class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class AttendentProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        
class DoctorProfileChange(UserChangeForm):
    class Meta:
        model = Doctor
        fields = "__all__" 
        

class TechnicianProfileChange(UserChangeForm):
    class Meta:
        model = Technician
        fields = "__all__" 

class ProfilePic(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic']
    
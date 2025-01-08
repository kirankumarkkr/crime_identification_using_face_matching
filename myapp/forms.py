
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Complaint, Criminal

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CriminalForm(forms.ModelForm):
    class Meta:
        model = Criminal
        fields = ['name', 'photo', 'description', 'date_of_birth','address', 'criminal_record']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['criminal' ,'complaint_no','crime_date', 'complaint_by','crime_location', 'criminal_contact' ]

class PhotoUploadForm(forms.Form):
    photo = forms.ImageField()
